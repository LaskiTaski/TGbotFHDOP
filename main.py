from aiogram.utils import executor
from bot_telegram import dp

from handlers.client import register_handlers_client

register_handlers_client(dp)


async def on_start_up(_):
    print('Start polling')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
