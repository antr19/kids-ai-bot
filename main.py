import os
from aiogram.utils import executor
from app import dp
from admin import handler
from models import attachment
from client import handler
from client import command_handler
from models.attachment import shutdown


async def on_start(_):
    if not os.path.exists("files"):
        os.mkdir("files")
    print('Система запущена!')


executor.start_polling(dp, skip_updates=True, on_startup=on_start, on_shutdown=shutdown)


