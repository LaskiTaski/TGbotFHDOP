from bot_telegram import bot
from aiogram import Dispatcher, types


# from keyboards.kb_client import keyboard_menu


# @dp.message_handler(commands=['start'], state='*') Эта часть кода обрабатывает команду /start
async def cmd_Start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    # kb.row(*keyboard_menu["Меню настроек"])

    await message.answer(text=message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Настройте стратегию для сортировки[ ](https://goo.su/VKUr)',
    #                        reply_markup=kb)


# @dp.message_handler() Эта часть кода обрабатывает приём любого текста.
async def cb_text(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    # kb.row(*keyboard_menu["Меню настроек"])

    await message.answer(text=message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text='Настройте стратегию для сортировки[ ](https://goo.su/VKUr)',
    #                        reply_markup=kb)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_Start, commands=["start"])
    dp.register_message_handler(cb_text)
    # dp.register_callback_query_handler(cb_Menu, text='Menu', state='*')
