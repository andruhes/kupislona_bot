from aiogram import types


button1 = types.KeyboardButton(text ='Инфо')
button2 = types.KeyboardButton(text ='Я сомневаюсь!')
button3 = types.KeyboardButton(text ='Купить слона, сегодня бесплатно')
button4 = types.KeyboardButton(text ='Лучше покажи лису')



keyboard1 = [
    [button1, button2],
    [button3], [button4]
]

keyboard2 = [
    [button3]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

