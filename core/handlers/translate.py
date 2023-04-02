from aiogram import Router, Bot
from aiogram.types import Message

from googletrans import Translator


router: Router = Router()  # routr init
translator: Translator = Translator()  # translator init


@router.message()  # triggered to send any message and translate it
async def process_translate(message: Message):
    result = translator.translate(text=message.text, src='auto', dest='en')
    await message.answer(text=result.text)
