from fastapi import status
from jwt import decode

from src.security import create_access_token, settings


def test_create_access_token_deve_criar_token():
    # Arrange
    data = {'sub': 'test@test.com'}

    # Act
    token = create_access_token(data)

    # Assert
    decoded = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert decoded['sub'] == data['sub']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token


def test_get_current_user_deve_retornar_401_quando_token_invalido(client):
    # Act
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_deve_retornar_401_quando_usuario_nao_encontrado(
    client, user, invalid_token
):
    # Act
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {invalid_token}'},
    )

    # Assert
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
