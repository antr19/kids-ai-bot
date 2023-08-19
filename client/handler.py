from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import os

import client.keyboard as kb
from app import dp, bot
from models.attachment import Attachment, session


@dp.message_handler(state='*', commands='start')
async def admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply('Приветики!', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='client_last_selfie')
async def get_last_selfie(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "selfie").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await callback.message.answer_photo(file, data.text)
    else:
        await callback.message.answer("Фотография ещё не загружена(")


@dp.callback_query_handler(text='client_graduation_photo')
async def get_graduation_photo(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "graduation").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await callback.message.answer_photo(file, data.text)
    else:
        await callback.message.answer("Фотография ещё не загружена(")


@dp.callback_query_handler(text='client_hobby_text')
async def get_last_hobby(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "hobby").one_or_none()
    if data:
        await callback.message.answer(data.text)
    else:
        await callback.message.answer("Рассказ ещё не загружен(")


@dp.callback_query_handler(text='client_description_GPT_voice')
async def get_GPT_voice(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "GPT_voice").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await callback.message.answer_voice(file, data.text)
    else:
        await callback.message.answer("Рассказ ещё не загружен(")


@dp.callback_query_handler(text='client_difference_SQL_NoSQL_voice')
async def get_sql_vs_nosql(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "sql_vs_nosql").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await callback.message.answer_voice(file, data.text)
    else:
        await callback.message.answer("Рассказ ещё не загружен(")


@dp.callback_query_handler(text='client_love_story')
async def get_love_story(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "love_story").one_or_none()
    if data:
        with open(data.path_to_file, 'rb') as file:
            await callback.message.answer_voice(file, data.text)
    else:
        await callback.message.answer("Рассказ ещё не загружен(")


@dp.callback_query_handler(text='client_link_to_repo')
async def get_repo(callback: types.CallbackQuery, state: FSMContext):
    data = session.query(Attachment).filter(Attachment.command == "repo").one_or_none()
    if data:
        await callback.message.answer(data.text)
    else:
        await callback.message.answer("Репозиторий ещё не загружен(")

