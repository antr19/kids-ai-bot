from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import copy

import admin.keyboard as kb
from app import dp, bot
from models.attachment import Attachment, session


class FSMloader(StatesGroup):
    selfie = State()
    graduation = State()
    hobby_text = State()
    gpt_voice = State()
    sql_vs_nosql = State()
    love_story = State()
    repo = State()


@dp.message_handler(commands='admin')
async def admin(message: types.Message):
    await message.reply('Добро пожаловать в интерфейс Админа!', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(state='*', text='admin_add_last_selfie')
async def add_last_selfie(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.selfie.set()
    await callback.message.answer("Пришли файлом фотографию, которую необходимо загрузить")


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMloader.selfie)
async def download_selfie(message: types.Message, state: FSMContext):
    path = "files/selfie.jpeg"
    try:
        await download_file(message, path)
    except AttributeError:
        await message.answer("Пришли, пожалуйста, именно ФАЙЛОМ фотографию")
        return
    data = {
        'command': 'selfie',
        'text': str(message.caption),
        'path_to_file': path
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Фотография успешно загружена и будет доступна в течение нескольких минут', reply_markup=kb.create_inkb_register())



@dp.callback_query_handler(text='admin_add_graduation_photo')
async def add_graduation_photo(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.graduation.set()
    await callback.message.answer("Пришли файлом фотографию, которую необходимо загрузить")


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMloader.graduation)
async def download_graduation(message: types.Message, state: FSMContext):
    path = "files/graduation.jpeg"
    try:
        await download_file(message, path)
    except AttributeError:
        await message.answer("Пришли, пожалуйста, именно ФАЙЛОМ фотографию")
        return
    data = {
        'command': 'graduation',
        'text': str(message.caption),
        'path_to_file': path
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Фотография успешно загружена и будет доступна в течение нескольких минут', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='admin_add_hobby_text')
async def add_hobby_text(callback : types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.hobby_text.set()
    await callback.message.answer("Пришли текст с описанием своего увлечения")


@dp.message_handler(state=FSMloader.hobby_text)
async def download_hobby(message: types.Message, state: FSMContext):
    data = {
        'command': 'hobby',
        'text': str(message.text),
        'path_to_file': ""
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Текст успешно сохранён', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='admin_add_description_GPT_voice')
async def add_description_gpt_voice(callback : types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.gpt_voice.set()
    await callback.message.answer("Запиши бабушке голосовое сообщение с описанием GPT")


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMloader.gpt_voice)
async def download_gpt_voice(message: types.Message, state: FSMContext):
    path = "files/GPT_voice.mp3"
    try:
        await download_voice(message, path)
    except AttributeError:
        await message.answer("Что-то пошло не так( Попробуй отправить ГС ещэ раз")
        return
    data = {
        'command': 'GPT_voice',
        'text': str(message.caption),
        'path_to_file': path
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Сообщение успешно загружено и будет доступно в течение нескольких минут', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='admin_add_difference_SQL_NoSQL_voice')
async def add_description_sql_vs_nosql_voice(callback : types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.sql_vs_nosql.set()
    await callback.message.answer("Объясни разницу между SQL и NoSQL")


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMloader.sql_vs_nosql)
async def download_sql_vs_nosql_voice(message: types.Message, state: FSMContext):
    path = "files/sql_vs_nosql.mp3"
    try:
        await download_voice(message, path)
    except AttributeError:
        await message.answer("Что-то пошло не так( Попробуй отправить ГС ещэ раз")
        return
    data = {
        'command': 'sql_vs_nosql',
        'text': str(message.caption),
        'path_to_file': path
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Сообщение успешно загружено и будет доступно в течение нескольких минут', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='admin_add_love_story')
async def add_description_love_story_voice(callback : types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.love_story.set()
    await callback.message.answer("Запиши в голосовом сообщении историю любви")


@dp.message_handler(content_types=types.ContentType.ANY, state=FSMloader.love_story)
async def download_love_story_voice(message: types.Message, state: FSMContext):
    path = "files/love_story.mp3"
    try:
        await download_voice(message, path)
    except AttributeError:
        await message.answer("Что-то пошло не так( Попробуй отправить ГС ещэ раз")
        return
    data = {
        'command': 'love_story',
        'text': str(message.caption),
        'path_to_file': path
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Сообщение успешно загружено и будет доступно в течение нескольких минут', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='admin_add_link_to_repo')
async def add_repo(callback : types.CallbackQuery, state: FSMContext):
    await state.finish()
    await FSMloader.repo.set()
    await callback.message.answer("Пришли ссылку на репозиторий")


@dp.message_handler(state=FSMloader.repo)
async def download_repo(message: types.Message, state: FSMContext):
    data = {
        'command': 'repo',
        'text': str(message.text),
        'path_to_file': ""
    }
    await add_to_db(Attachment(**data))
    await state.finish()
    await message.answer('Текст успешно сохранён', reply_markup=kb.create_inkb_register())


@dp.callback_query_handler(text='admin_reset')
async def reset(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    defaults = session.query(Attachment).filter(Attachment.command.like("%_backup")).all()
    for backup in defaults:
        backup.command.replace("_backup", "")
        session.add(backup)
        session.commit()
    await callback.message.answer("Все файлы вернулись в изначальное состояние")


async def download_file(message: types.Message, path: str):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, path)


async def download_voice(message: types.Message, path: str):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, path)


async def add_to_db(att: Attachment):
    old = session.query(Attachment).filter(Attachment.command == att.command).one_or_none()
    if old:
        old.text = att.text if att.text else old.text
        old.path_to_file = att.path_to_file if att.path_to_file else old.path_to_file
        session.add(old)
    else:
        session.add(att)

        backup = copy.deepcopy(att)
        backup.command = backup.command + "_backup"
        session.add(backup)

    session.commit()
