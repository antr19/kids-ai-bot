from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from app import dp, bot
from models.attachment import Attachment, session


@dp.message_handler(commands='last_selfie')
async def get_last_selfie(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "selfie").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await message.answer_photo(file, data.text)
    else:
        await message.answer("Фотография ещё не загружена(")


@dp.message_handler(commands='graduation_photo')
async def get_graduation_photo(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "graduation").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await message.answer_photo(file, data.text)
    else:
        await message.answer("Фотография ещё не загружена(")


@dp.message_handler(commands='hobby_text')
async def get_last_hobby(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "hobby").one_or_none()
    if data:
        await message.answer(data.text)
    else:
        await message.answer("Рассказ ещё не загружен(")


@dp.message_handler(commands='description_gpt_voice')
async def get_GPT_voice(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "GPT_voice").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await message.answer_voice(file, data.text)
    else:
        await message.answer("Рассказ ещё не загружен(")


@dp.message_handler(commands='sql_vs_nosql_voice')
async def get_sql_vs_nosql(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "sql_vs_nosql").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await message.answer_voice(file, data.text)
    else:
        await message.answer("Рассказ ещё не загружен(")


@dp.message_handler(commands='love_story')
async def get_love_story(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "love_story").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await message.answer_voice(file, data.text)
    else:
        await message.answer("Рассказ ещё не загружен(")


@dp.message_handler(commands='link_to_repo')
async def get_repo(message: types.Message, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "repo").one_or_none()
    if data:
        await message.answer(data.text)
    else:
        await message.answer("Репозиторий ещё не загружен(")
