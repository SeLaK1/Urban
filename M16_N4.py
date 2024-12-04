from typing import List
from fastapi import FastAPI, Path, Form, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int = None

@app.get('/users')
async def get_all_user() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int, user: User = None) -> User:
    try:
        if users != []:
            user.id = users[-1].id + 1
        else:
            user.id = 1
        user.username = username
        user.age = age
        users.append(user)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        update_user = users[user_id-1]
        update_user.username = username
        update_user.age = age
        return update_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/user/{user_id}')
async def delete_message(user_id: int) -> User:
    index = -1
    for user in users:
        index += 1
        if user.id == user_id:
            users.pop(index)
            return user
    raise HTTPException(status_code=404, detail='User not found')





