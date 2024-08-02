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
from apps.bot.handers import register_handlers


async def _start_bot(bot_id: int) -> None:
    from apps.bot.models import GroupBot
    group_bot = await sync_to_async(GroupBot.objects.get)(pk=bot_id)

    bot_token = group_bot.token
    bot_name = group_bot.name
    dp = Dispatcher()

    register_handlers(dp)
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
    from apps.bot.models import GroupBot
    group_bot = await sync_to_async(GroupBot.objects.get)(pk=bot_id)

    bot_token = group_bot.token
    dp = Dispatcher()
    bot = Bot(token=bot_token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.stop_polling(bot, polling_timeout=20,)
