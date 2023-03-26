from aiogram import Bot
from aiogram.types import BotCommand

from core.lexicon import LEXICON_CMD_EN


async def set_main_manu(bot: Bot):  # create nemu
    main_menu_cmds = [BotCommand(command=command,
                                 description=description)
                      for command, description in LEXICON_CMD_EN.items()]
    await bot.set_my_commands(main_menu_cmds)
