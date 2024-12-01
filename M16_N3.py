from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_user() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f'User {username} is registred'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {username} is updated'

@app.delete('/user/{user_id}')
async def delete_message(user_id: int) -> str:
    users.pop(user_id)
    return f'User with {user_id} was deleted'




