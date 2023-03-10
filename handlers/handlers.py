from aiogram import Router, Bot
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from lexicon.lexicon import LEXICON_EN
from googletrans import Translator


router: Router = Router()
translator: Translator = Translator()


@router.message(CommandStart())
async def process_cmd_start(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON_EN['start'])


@router.message(Command(commands='help'))
async def process_cmd_help(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON_EN['help'])


@router.message(Text(startswith='en ', ignore_case=True))
async def process_translate(message: Message):
    result = translator.translate(text=message.text[3:], src='auto', dest='en')
    await message.answer(text=result.text)


@router.message(Text(startswith='ru ', ignore_case=True))
async def process_translate(message: Message):
    result = translator.translate(text=message.text[3:], src='auto', dest='ru')
    await message.answer(text=result.text)


@router.message(Text(startswith='de ', ignore_case=True))
async def process_translate(message: Message):
    result = translator.translate(text=message.text[3:], src='auto', dest='de')
    await message.answer(text=result.text)


@router.message()
async def not_select_language(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await message.answer(text=LEXICON_EN['no_lang'])
