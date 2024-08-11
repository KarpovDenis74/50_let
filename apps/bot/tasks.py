import asyncio
from concurrent.futures import ThreadPoolExecutor

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from celery import shared_task

from apps.bot.handlers import router

from asgiref.sync import sync_to_async


async def get_group_bot(bot_id: int):
    from apps.bot.models import GroupBot
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool,
                                          lambda: (GroupBot
                                                   .objects
                                                   .get(pk=bot_id)))


async def _start_bot(bot_id: int) -> None:
    group_bot = await get_group_bot(bot_id)

    bot_token = group_bot.token
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


# async def _stop_bot(bot_id: int) -> None:
#     group_bot = await get_group_bot(bot_id)
#     bot_token = group_bot.token

#     loop = asyncio.get_event_loop()
#     print(f'{loop=}')
#     for task in asyncio.all_tasks(loop):
#         task.cancel()
#     loop.stop()


# @shared_task
# def stop_bot(bot_id) -> None:
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(_stop_bot(bot_id))
#     # group_bot = await get_group_bot(bot_id)
#     # bot_token = group_bot.token

#     loop = asyncio.get_event_loop()
#     sync_to_async(print(f'{loop=}'))
#     for task in asyncio.all_tasks(loop):
#         task.cancel()
#     loop.stop()
