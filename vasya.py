import asyncio
import json
import logging
import os
import sys
from time import sleep

import requests
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = os.getenv('BOT_TOKEN')
I_TOKEN = os.getenv('I_TOKEN')
print(f'{I_TOKEN=}')
FOLDER_ID = os.getenv('FOLDER_ID')
BOT_NAME = os.getenv('BOT_NAME')
dp = Dispatcher()
IAM_TOKEN = json.loads(
    requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens',
                  data=json.dumps({'yandexPassportOauthToken': f'{I_TOKEN}'}))
    .text)['iamToken']
print(IAM_TOKEN)


def answer_generator(question: str) -> str:
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {IAM_TOKEN}',
               'x-folder-id': FOLDER_ID}
    data = json.dumps({
        'modelUri': f'gpt://{FOLDER_ID}/yandexgpt-lite',
        'completionOptions': {'stream': False,
                              'temperature': 0.1,
                              'maxTokens': '200'},
        'messages': [
            {'role': 'system',
                'text': 'Ты профессионал в области  безопасности (Россия)'},
            {'role': 'user',
                'text': f'{question}'}
        ]
    })
    response = requests.post(
        'https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync',
        headers=headers, data=data
    )
    print(f'{response.text}')
    if response.status_code == 200:
        answer = json.loads(response.text)
        print(f'{answer=}')
        id = answer["id"]
        while not answer['done']:
            headers = {'Authorization': f'Bearer {IAM_TOKEN}'}
            response = requests.get(
                f'https://llm.api.cloud.yandex.net/operations/{id}',
                headers=headers
            )
            answer = json.loads(response.text)
            sleep(3)
            print(f'{      type(answer)=}')
    else:
        return False
    print(f'{           type(answer)=}')
    print(f'{           answer=}')
    return answer['response']['alternatives'][0]['message']['text']


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        question = message.text.lower()
        if question.startswith(BOT_NAME):
            question = question.replace(BOT_NAME, '')
            answer = answer_generator(question)
            if answer:
                await message.answer(text=str(answer))
    except TypeError:
        await message.answer('Что то пошло не так')


async def main() -> None:
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot, polling_timeout=20,)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
