from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_inkb_register():
    inkb = InlineKeyboardMarkup(row_width=1)
    inkb.add(InlineKeyboardButton(text='🔸 Последнее селфи', callback_data='client_last_selfie'))
    inkb.add(InlineKeyboardButton(text='🔸 Фотография с выпускного', callback_data='client_graduation_photo'))
    inkb.add(InlineKeyboardButton(text='🔸 Пост об увлечении', callback_data='client_hobby_text'))
    inkb.add(InlineKeyboardButton(text='🔸 Гс с описанием GPT', callback_data='client_description_GPT_voice'))
    inkb.add(InlineKeyboardButton(text='🔸 Гс с описанием разницы SQL и NoSQL', callback_data='client_difference_SQL_NoSQL_voice'))
    inkb.add(InlineKeyboardButton(text='🔸 Гс с историей любви', callback_data='client_love_story'))
    inkb.add(InlineKeyboardButton(text='🔸 Ссылка на репозиторий', callback_data='client_link_to_repo'))
    return inkb