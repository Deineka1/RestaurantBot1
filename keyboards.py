from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btnMain = KeyboardButton('Главное меню')

#Кнопки главного меню
b2 = KeyboardButton('Меню Администратора')
b1 = KeyboardButton('/test')
b3 = KeyboardButton('Меню Клиента')
kb_Main = ReplyKeyboardMarkup(resize_keyboard=True).row(b2, b3)
kb_test = ReplyKeyboardMarkup(resize_keyboard=True).add(b1).add(btnMain)

#Кнопки меню клиента
b4 = KeyboardButton('На месте')
b5 = KeyboardButton('С собой')
b6 = KeyboardButton('Доставка')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True).row(b4, b5, b6).add(btnMain)

#Кнопки меню На месте
b7 = KeyboardButton('Официант')
b8 = KeyboardButton('Меню')
b9 = KeyboardButton('Счет')
kb_nameste = ReplyKeyboardMarkup(resize_keyboard=True).row(b7, b8, b9).add(btnMain)

#Кнопки меню С собой
b10 = KeyboardButton('*Меню')
kb_ssoboy = ReplyKeyboardMarkup(resize_keyboard=True).row(b10).add(btnMain)

#Кнопки меню Доставка
b11 = KeyboardButton('*Меню*')
b12 = KeyboardButton('Посмотреть заказ')
kb_dostavka = ReplyKeyboardMarkup(resize_keyboard=True).row(b11, b12).add(btnMain)


#Кнопки меню админа
b13 = KeyboardButton('Доставки')
b14 = KeyboardButton('Ресторан')
b15 = KeyboardButton('Прибыль')
b16 = KeyboardButton('Отчет')
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(b13, b14, b15, b16).add(btnMain)
