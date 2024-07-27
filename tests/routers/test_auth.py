from fastapi import status


def test_login_deve_retornar_token(client, user):
    # Act
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert token['token_type'] == 'Bearer'
    assert 'access_token' in token


def test_login_deve_retornar_400_se_usuario_nao_for_encontrado(client):
    # Act
    response = client.post(
        '/auth/token',
        data={
            'username': 'bad_username@email.com',
            'password': '123',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_login_deve_retornar_400_se_senha_for_invalida(client, user):
    # Act
    response = client.post(
        '/auth/token',
        data={
            'username': user.email,
            'password': 'xpto',
        },
    )

    # Assert
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {'detail': 'Incorrect email or password'}
