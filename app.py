import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.types import FSInputFile
import os

token = os.getenv("TOKEN")

storage = MemoryStorage()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher(bot, storage=storage)

# Хэндлер на команду /start
@dp.message_handler(commands='start2')
async def cmd_start(message: types.Message):
    with open("cat.jpeg", 'rb') as cat:
        await message.reply_photo(cat, "Hello!")
    with open("voice.mp3", 'rb') as voice:
        await message.reply_voice(voice)
