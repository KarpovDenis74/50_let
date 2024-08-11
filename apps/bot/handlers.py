import asyncio
from concurrent.futures import ThreadPoolExecutor

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from asgiref.sync import sync_to_async

from apps.bot.utils import AssistantUtils

router = Router()


def b(bot_chat_id, question):
    from apps.bot.models import GroupBot
    assistant = GroupBot.objects.filter(group_id=bot_chat_id).first().assistant
    a = AssistantUtils(assistant)
    return a.get_answer(question)


async def get_group_bot(bot_chat_id, question):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool,
                                          b(bot_chat_id, question))


@router.message(Command(commands=['start']))
async def send_welcome(message: Message):

    await message.answer("Hello!")


@router.message(lambda message: message.text is not None)
async def echo(message: Message):
    answer = await sync_to_async(b)(message.chat.id, message.text)
    await message.answer(answer)
