import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import handlers
from keyboards.main_menu import set_main_manu


async def main():
    logging.basicConfig(level=logging.INFO)  # console updates

    token: Config = load_config()            # load bot token

    bot: Bot = Bot(token=token.tg_bot.token, parse_mode='HTML')  # init bot
    dp: Dispatcher = Dispatcher()                                # init dispatcher

    await set_main_manu(bot)            # main menu init

    dp.include_router(handlers.router)  # registration of routers in the dispatcher

    await bot.delete_webhook(drop_pending_updates=True)  # delete old updates
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
