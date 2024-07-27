from fastapi import status

from src.schemas import UserPublic


def test_create_user_deve_criar_usuario_e_retornar_dados_com_id(client):
    # Act
    response = client.post(
        '/users',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_create_user_deve_retornar_400_se_username_ja_existir(client, user):
    # Act
    response = client.post(
        '/users',
        json={
            'username': user.username,
            'password': 'password',
            'email': 'random@test.com',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Username already exists'}


def test_create_user_deve_retornar_400_se_email_ja_existir(client, user):
    # Act
    response = client.post(
        '/users',
        json={
            'username': 'xpto_random',
            'password': 'password',
            'email': user.email,
        },
    )

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Email already exists'}


def test_get_users_deve_retornar_lista_vazia(client):
    # Act
    response = client.get('/users')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'users': []}


def test_get_users_deve_retornar_lista_com_dados(client, user):
    # Arrange
    user_schema = UserPublic.model_validate(user).model_dump()

    # Act
    response = client.get('/users')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'users': [user_schema]}


def test_get_user_by_id_deve_retornar_404_se_usuario_nao_existir(client, user):
    # Act
    response = client.get('/users/999')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_by_id_deve_retornar_usuario(client, user):
    # Arrange
    user_schema = UserPublic.model_validate(user).model_dump()

    # Act
    response = client.get('/users/1')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == user_schema


def test_update_user_deve_atualizar_usuario_e_retornar_dado_atualizado(
    client, user, token
):
    # Act
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'testusername2',
            'password': '123',
            'email': 'test@test.com',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': user.id,
    }


def test_update_user_deve_retornar_403_ao_atualizar_outro_usuario(
    client, other_user, token
):
    # Act
    response = client.put(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'testusername2',
            'password': '123',
            'email': 'test@test.com',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_user_deve_retornar_204_ao_excluir_usuario(client, user, token):
    # Act
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    # Assert
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_user_deve_retornar_403_ao_remover_outro_usuario(
    client, other_user, token
):
    # Act
    response = client.delete(
        f'/users/{other_user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    # Assert
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
