from typing import Annotated
from fastapi import FastAPI, Path

#http://127.0.0.1:8000/docs

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'messsage': 'Главная страница'}


@app.get('/user/admin')
async def admin() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def get_user(user_id: Annotated[int, Path(ge=0, le=100, description='Enter User ID', example='2')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
               age: int = Path(ge=18, le=120, description='Enter age', example='45')) -> dict:
    return {'message': f'Информация о пользователе Имя: {username} Возраст: {age}'}
