import time

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from crud_functions import *


api = '7973596512:AAEQe3y7USAQ98mJt_r2nyPbYlS5aqAwATo'
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())

klava1 = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = 'Информация'),
         KeyboardButton(text = 'Рассчитать')],
        [KeyboardButton(text = 'Купить')]
    ], resize_keyboard = True
)

klava2 = InlineKeyboardMarkup(resize_keyboard = True)
button1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
klava2.add(button1)
klava2.add(button2)

klava3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт4', callback_data='product_buying')]
    ]
)

products = get_all_products()


class User(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def nachalo(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup = klava1)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    number = 0
    for product in products:
        number+= 1
        with open(f'pictchers/{number}.png', 'rb') as img:
            await message.answer_photo(img, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        time.sleep(1)
    await message.answer('Выберите продукт для покупки:', reply_markup = klava3)

@dp.message_handler(text = 'Информация')
async def nachalo(message):
    await message.answer('Доброго времени суток, я бот, способный рассчитать нужную суточную норму '
                         'калорий для тебя, чтобы это сделать, нажми на кнопку "Рассчитать" ')

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = klava2)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно преобрели препарат!')
    await call.answer()

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10*вес(кг) + 6,25*рост(см) - 5*возраст(г)-161')

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
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