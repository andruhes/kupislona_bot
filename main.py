
import asyncio
import logging
import config
import random
import os  # Импортируем os для проверки существования файла
from keyboards import kb1, kb2
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import InputFile
from slon import fox





# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объект бота
bot = Bot(token=config.token)

# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)
    await message.answer(f' Сегодня твой счастливый день, ты купишь слона! ')





# Текстовое представление слона с исправленным выравниванием
elephant_art = r"""
.       /  \\
       / ..|\\
      (_\  |_)
      /   \@'
     /      \\
    /  _    _\\
   /  / \  / \\
  /__/   \/   \\
"""

@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name  # Получаем имя пользователя
    if 'слон' in msg_user:
        await message.answer(elephant_art)
        await message.answer(f'Держи слона! {name}')
        await message.answer(f'Сегодня бесплатно!')
    elif 'инфо' in msg_user:
        await message.answer(f'Я бот и мне очень хочется продать тебе слона,  {name}')
    elif 'сомневаюсь' in msg_user:
        await message.answer(f'Поверь, такого слона ты еще не покупал,  {name}')
    elif 'закрыть' in msg_user:
        await message.answer(f'Не хочу закрываться, лучше попроси показать тебе лису')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я бот Андрея М')
    elif 'ты робот' in msg_user:
        await message.answer(f'Я бот Андрея М')
    elif 'еще слона' in msg_user:
        await message.answer(f'Кстати купи еще, у меня много')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я бот. Ваш текст для меня малоразборчив')
    elif 'лису' in msg_user:
        img_fox = fox()
        await message.answer(f'Держи лису, {name}')
        await message.answer_photo(photo=img_fox)
        await message.answer(f'А теперь купишь слона? {name}', reply_markup=kb1)
    else:
        await message.answer(f'Ой все! Купи слона и заживи яркой жизнью!')
        await message.answer(f'А теперь купишь слона? {name}', reply_markup=kb1)



# Запуск бота
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())