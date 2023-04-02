from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from core.lexicon.lexicon import LEXICON_EN
from googletrans import Translator


router: Router = Router()  # routr init


@router.message(CommandStart())  # triggered to send start
async def process_cmd_start(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON_EN['start'])
