from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.answer("Hello!")