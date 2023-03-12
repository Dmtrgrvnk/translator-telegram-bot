from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from core.lexicon.lexicon import LEXICON_EN
from googletrans import Translator


router: Router = Router()
translator: Translator = Translator()


@router.message(CommandStart())
async def process_cmd_start(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON_EN['start'])


@router.message()
async def process_translate(message: Message):
    result = translator.translate(text=message.text, src='auto', dest='en')
    await message.answer(text=result.text)
