from aiogram.utils import executor
# from bot_telegram import dp




async def on_start_up(_):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)

