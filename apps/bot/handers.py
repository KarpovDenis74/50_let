from aiogram.types import Message
from aiogram import Dispatcher


async def echo_handler(message: Message) -> None:
    await message.answer(text=str('Привет'))


def register_handlers(dp: Dispatcher):
    dp.register_message(echo_handler)
