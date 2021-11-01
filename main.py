from aiogram import Bot, Dispatcher, types, executor
import keyboards as nav
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

Token = '*****************'

storage = MemoryStorage()

bot = Bot(token=Token)
dp = Dispatcher(bot, storage=storage)


class Admin(StatesGroup):
    login = State()
    password = State()
    markups = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствуем Вас!', reply_markup=nav.kb_Main)


@dp.message_handler(Command('test'), state=None)
async def process_input(message: types.Message):
    print('Ждем логин')
    await message.answer('Введите логин')
    print('1')
    await Admin.login.set()
    print('2')


@dp.message_handler(state=Admin.login)  # Принимаем ответ на логин
async def answer_login(message: types.Message, state: FSMContext):
    print('Записали логин')
    login = message.text
    if login == '111':
        print('Ввели правильный логин')
        await state.update_data({'answer1': login})
        await message.answer('Введите пароль')
        await message.delete()
        await Admin.password.set()

    else:
        print('Ошибка логина')
        await message.answer('Пользователя с таким логином не существует', reply_markup=nav.kb_Main)
        await state.finish()


@dp.message_handler(state=Admin.password)  # Принимаем ответ на пароль
async def answer_password(message: types.Message, state: FSMContext):
    password = message.text
    if password == '222':
        print('УРА')
        await state.update_data({'answer2': password})
        await message.answer('Вы зашли в меню администратора', reply_markup=nav.kb_admin)
        await message.delete()
        await Admin.markups.set()
    else:
        print('Ошибка пароля')
        await message.answer('Не верный пароль', reply_markup=nav.kb_Main)
        await state.finish()


@dp.message_handler(state=Admin.markups)  # Принимаем ответ на кнопки
async def answer_markups(message: types.Message, state: FSMContext):
    if message.text == 'Меню администратора':
        await message.answer('Меню администратора', reply_markup=nav.kb_admin)
        await state.finish()
    elif message.text == 'Доставки':
        await message.answer('Доставки на сегодня: ', reply_markup=nav.kb_admin)
    elif message.text == 'Ресторан':
        await message.answer('Заказы на сегодня: ', reply_markup=nav.kb_admin)
    elif message.text == 'Прибыль':
        await message.answer('Прибыль составляет: ', reply_markup=nav.kb_admin)
    elif message.text == 'Отчет':
        await message.answer('Отчет за сегодня: ', reply_markup=nav.kb_admin)
    else:
        await bot.send_message(message.from_user.id, 'Я Вас не понимать', reply_markup=nav.kb_Main)
        await state.finish()


@dp.message_handler()
async def process_start_command(message: types.Message):
    if message.text == 'Меню Клиента':
        await bot.send_message(message.from_user.id, 'Меню клиента', reply_markup=nav.kb_client)
    elif message.text == 'На месте':
        await bot.send_message(message.from_user.id, 'Что Вам принести?', reply_markup=nav.kb_nameste)
    elif message.text == 'Официант':
        await bot.send_message(message.from_user.id, 'Официант подойдет в ближайшее время ')
    elif message.text == 'Меню':
        await bot.send_message(message.from_user.id, 'Выберете блюдо')
    elif message.text == 'Счет':
        await bot.send_message(message.from_user.id, 'Счет')
    elif message.text == 'С собой':
        await bot.send_message(message.from_user.id, 'Выберите блюдо из меню', reply_markup=nav.kb_ssoboy)
    elif message.text == '*Меню':
        await bot.send_message(message.from_user.id, 'Выберете блюдо')
    elif message.text == 'Доставка':
        await bot.send_message(message.from_user.id, 'Доставляем все втечение часа!', reply_markup=nav.kb_dostavka)
    elif message.text == '*Меню*':
        await bot.send_message(message.from_user.id, 'Выберете блюдо')
    elif message.text == 'Посмотреть заказ':
        await bot.send_message(message.from_user.id, 'Ваш заказ: ')
    elif message.text == 'Меню Администратора':
        await bot.send_message(message.from_user.id, 'Чтобы зайти в меню администратора, нажмите /test',
                               reply_markup=nav.kb_test)
    elif message.text == 'Меню клиента':
        await bot.send_message(message.from_user.id, 'Вы вернулись в Меню клиента', reply_markup=nav.kb_client)
    else:
        await bot.send_message(message.from_user.id, 'Я Вас не понимать', reply_markup=nav.kb_Main)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
