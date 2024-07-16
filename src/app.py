from fastapi import FastAPI, HTTPException, status

from src.schemas import UserDb, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.post(
    '/users', status_code=status.HTTP_201_CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDb(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get('/users', status_code=status.HTTP_200_OK, response_model=UserList)
def get_users():
    return {'users': database}


@app.get(
    '/users/{user_id}',
    response_model=UserPublic,
    responses={status.HTTP_404_NOT_FOUND: {'detail': 'User not found'}},
)
def get_user_by_id(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    user = database[user_id - 1]
    return user


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDb(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]
