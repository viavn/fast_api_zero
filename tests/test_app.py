from fastapi import status


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


def test_get_users_deve_retornar_ok_e_usuarios(client):
    # Act
    response = client.get('/users')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_get_user_by_id_deve_retornar_404_se_id_for_maior_que_lista(client):
    # Act
    response = client.get('/users/999')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_by_id_deve_retornar_404_se_id_for_menor_que_1(client):
    # Act
    response = client.get('/users/0')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_get_user_by_id_deve_retornar_usuario(client):
    # Act
    response = client.get('/users/1')

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_update_user_deve_atualizar_usuario_e_retornar_dado_atualizado(client):
    # Act
    response = client.put(
        '/users/1',
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
        'id': 1,
    }


def test_update_user_deve_retornar_404_se_id_for_maior_que_lista(client):
    # Act
    response = client.put(
        '/users/999',
        json={
            'username': 'testusername2',
            'password': '123',
            'email': 'test@test.com',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user_deve_retornar_404_se_id_for_menor_que_1(client):
    # Act
    response = client.put(
        '/users/0',
        json={
            'username': 'testusername2',
            'password': '123',
            'email': 'test@test.com',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_404_se_id_for_maior_que_lista(client):
    # Act
    response = client.delete('/users/999')

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_404_se_id_for_menor_que_1(client):
    # Act
    response = client.delete(
        '/users/0',
    )

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_deve_retornar_204_ao_excluir_usuario(client):
    # Act
    response = client.delete('/users/1')

    # Assert
    assert response.status_code == status.HTTP_204_NO_CONTENT
