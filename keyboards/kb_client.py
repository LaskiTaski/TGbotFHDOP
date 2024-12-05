from aiogram import types

article = types.InlineKeyboardButton(text='Статья на что-то🚁', callback_data='Article')
youtube = types.InlineKeyboardButton(text='Ссылка на наш YouTube', callback_data='YouTube')

my_keyboards = {
    'Статья': article,
    'Ссылка': youtube
}
