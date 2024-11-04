from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from  aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

klava = ReplyKeyboardMarkup()
button_1 = KeyboardButton(text = 'Информация')
button_2 = KeyboardButton(text = 'Рассчитать')
klava.add(button_1)
klava.add(button_2)

class User(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def nachalo(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup = klava)

@dp.message_handler(text = 'Информация')
async def nachalo(message):
    await message.answer('Доброго времени суток, я бот, способный рассчитать нужную суточную норму '
                         'калорий для тебя, чтобы это сделать, нажми на кнопку "Рассчитать" ')

@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст')
    await User.age.set()

@dp.message_handler(state=User.age)
async def set_growth(message, state):
    await state.update_data(age = int(message.text))
    await message.answer('Введите свой рост')
    await User.growth.set()

@dp.message_handler(state=User.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес')
    await User.weight.set()

@dp.message_handler(state=User.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    calorie = 10*data['weight']+6.25*data['growth']-5*data['age']+5
    await message.answer(f"Ваше оптимальное количество калорий: {calorie}")
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
