from bot_telegram import bot
from aiogram import Dispatcher, types

# from keyboards.kb_client import keyboard_menu
from database.db_client import upgrade_register_user
from keyboards.kb_client import my_keyboards

from datetime import datetime

client_data = []


# @dp.message_handler(commands=['start'], state='*') Эта часть кода обрабатывает команду /start
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(my_keyboards['Статья'])
    kb.row(my_keyboards['Ссылка'])

    InformationUser = {
        "UserID": message.from_user.id,
        "Name": message.from_user.first_name,
        "UserName": message.from_user.username,
        "Registration": datetime.now().strftime("%d.%m.%Y")
    }

    upgrade_register_user(InformationUser)

    await bot.send_message(chat_id=message.from_user.id,
                           text='Смотри какой у нас котик[ ](https://clck.ru/3Etbeu)',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_Menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(my_keyboards['Статья'])
    kb.row(my_keyboards['Ссылка'])

    InformationUser = {
        "UserID": callback.from_user.id,
        "Name": callback.from_user.first_name,
        "UserName": callback.from_user.username,
        "Registration": datetime.now().strftime("%d.%m.%Y")
    }

    upgrade_register_user(InformationUser)

    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Смотри какой у нас котик[ ](https://clck.ru/3Etbeu)',
    #                        reply_markup=kb)

    await callback.message.edit_text('Смотри какой у нас котик[ ](https://clck.ru/3Etbeu)',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='Article', state='*')
async def cb_Article(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.row(my_keyboards['Ссылка'])
    kb.row(my_keyboards['Меню'], my_keyboards['Ссылка'])
    kb.row(my_keyboards['Ссылка'], my_keyboards['Меню'], my_keyboards['Ссылка'])
    kb.row(my_keyboards['Ссылка'])
    kb.row(my_keyboards['Пустышка'])
    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='YouTube', state='*')
async def cb_YouTube(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.row(my_keyboards['Статья'])
    kb.row(my_keyboards['Меню'])

    await callback.message.edit_text('[Информация о боте](https://telegra.ph/Informaciya-o-bote-03-19)',
                                     reply_markup=kb)


# # @dp.message_handler() Эта часть кода обрабатывает приём любого текста.
# async def cb_text(message: types.Message):
#     kb = types.InlineKeyboardMarkup(row_width=1)
#     # kb.row(*keyboard_menu["Меню настроек"])
#
#     await message.answer(text=message.text)
#     # await bot.send_message(chat_id=message.from_user.id,
#     #                        text='Настройте стратегию для сортировки[ ](https://goo.su/VKUr)',
#     #                        reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=["start"])
    dp.register_callback_query_handler(cb_Menu, text='Menu', state='*')

    dp.register_callback_query_handler(cb_Article, text='Article', state='*')
    dp.register_callback_query_handler(cb_YouTube, text='YouTube', state='*')

