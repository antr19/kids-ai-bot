from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_inkb_register():
    inkb = InlineKeyboardMarkup(row_width=1)
    inkb.add(InlineKeyboardButton(text='🔹 Добавить последнее селфи', callback_data='admin_add_last_selfie'))
    inkb.add(InlineKeyboardButton(text='🔹 Добавить фотографию с выпускного', callback_data='admin_add_graduation_photo'))
    inkb.add(InlineKeyboardButton(text='🔹 Добавить пост об увлечении', callback_data='admin_add_hobby_text'))
    inkb.add(InlineKeyboardButton(text='🔹 Добавить гс с описанием GPT', callback_data='admin_add_description_GPT_voice'))
    inkb.add(InlineKeyboardButton(text='🔹 Добавить гс с описанием разницы SQL и NoSQL', callback_data='admin_add_difference_SQL_NoSQL_voice'))
    inkb.add(InlineKeyboardButton(text='🔹 Добавить гс с историей любви', callback_data='admin_add_love_story'))
    inkb.add(InlineKeyboardButton(text='🔹 Добавить ссылку на репозиторий', callback_data='admin_add_link_to_repo'))
    inkb.add(InlineKeyboardButton(text='🔹 Вернуть всё назад', callback_data='admin_reset'))
    return inkb