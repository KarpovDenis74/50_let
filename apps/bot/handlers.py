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
    bot = GroupBot.objects.filter(group_id=bot_chat_id).first()
    assistant = bot.assistant
    if question.lower().startswith(bot.name.lower()):
        a = AssistantUtils(assistant)
        return a.get_answer(question)
    else:
        return None


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
    print(f'{answer=}')
    if answer is not None:
        await message.reply(text=answer, parse_mode='markdown',
                            disable_web_page_preview=True)
