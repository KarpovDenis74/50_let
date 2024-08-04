import asyncio
import json

import requests
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from asgiref.sync import sync_to_async
from celery import shared_task
from apps.bot.handlers import router
from concurrent.futures import ThreadPoolExecutor


async def get_group_bot(bot_id: int):
    from apps.bot.models import GroupBot
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, lambda: GroupBot.objects.get(pk=bot_id))


async def _start_bot(bot_id: int) -> None:
    from apps.bot.models import GroupBot
    group_bot = await get_group_bot(bot_id)

    bot_token = group_bot.token
    bot_name = group_bot.name
    dp = Dispatcher()

    dp.include_router(router)
    bot = Bot(token=bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot, polling_timeout=20,)

@shared_task
def start_bot(bot_id: int):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_start_bot(bot_id))

    # asyncio.run(_start_bot(bot_id))


@shared_task
async def stop_bot(bot_id):
    group_bot = await get_group_bot(bot_id)
    bot_token = group_bot.token
    dp = Dispatcher()
    bot = Bot(token=bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.stop_polling()
