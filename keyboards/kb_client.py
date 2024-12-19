from aiogram import types

menu = types.InlineKeyboardButton(text='🔙', callback_data='Menu')

article = types.InlineKeyboardButton(text='Статья на что-то🚁', callback_data='Article')
youtube = types.InlineKeyboardButton(text='Ссылка на наш YouTube', callback_data='YouTube')
passi = types.InlineKeyboardButton(text='Кнопка пустышка просто есть', callback_data='YouTube')

my_keyboards = {
    'Меню': menu,
    'Статья': article,
    'Ссылка': youtube,
    'Пустышка': passi
}
