import pytest
from sqlalchemy import select

from src.models import User


@pytest.mark.vini
def test_create_user(session):
    # Arrange
    user = User(username='viavn', email='vi@email.com', password='password')

    # Act
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'vi@email.com'))

    # Assert
    assert result.username == 'viavn'
