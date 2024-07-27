from fastapi import status
from freezegun import freeze_time


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


def test_token_expired_after_time(client, user):
    # Act
    with freeze_time('2023-07-14 12:00:00'):
        # Gerar o token (12:00)
        response = client.post(
            '/auth/token',
            data={'username': user.email, 'password': user.clean_password},
        )
        assert response.status_code == status.HTTP_200_OK
        token = response.json()

    with freeze_time('2023-07-14 12:31:00'):
        # Usando o token (12:31)
        response = client.put(
            f'/users/{user.id}',
            headers={'Authorization': f'Bearer {token}'},
            json={
                'username': 'testusername2',
                'password': '123',
                'email': 'test@test.com',
            },
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}


def test_refresh_token(client, token):
    # Act
    response = client.post(
        '/auth/refresh_token',
        headers={'Authorization': f'Bearer {token}'},
    )

    data = response.json()

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert 'access_token' in data
    assert 'token_type' in data
    assert data['token_type'] == 'bearer'


def test_token_expired_dont_refresh(client, user):
    with freeze_time('2023-07-14 12:00:00'):
        response = client.post(
            '/auth/token',
            data={'username': user.email, 'password': user.clean_password},
        )
        assert response.status_code == status.HTTP_200_OK
        token = response.json()['access_token']

    with freeze_time('2023-07-14 12:31:00'):
        response = client.post(
            '/auth/refresh_token',
            headers={'Authorization': f'Bearer {token}'},
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() == {'detail': 'Could not validate credentials'}
