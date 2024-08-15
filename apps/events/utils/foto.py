from django.conf import settings
from telethon import TelegramClient, utils
from telethon.tl.types import InputMessagesFilterPhotos


class TUtils:
    TG_SESSION_NAME = 'SESSION1'
    client = TelegramClient(TG_SESSION_NAME, settings.API_ID,
                            settings.API_HASH)

    def __init__(self, bot):
        self.bot = bot
        self.group_id = self.bot.group_id

    def _get_group_peer(self):
        real_id, peer_type = utils.resolve_id(int(self.group_id))

        print(real_id)  # 456
        print(peer_type)  # <class 'telethon.tl.types.PeerChannel'>

        peer = peer_type(real_id)
        print(peer)  # PeerChannel(channel_id=456)
        return peer

    async def get_history(self):
        all_messages = []
        offset_id = 0
        while True:

            async with TelegramClient(self.TG_SESSION_NAME, settings.API_ID,
                                      settings.API_HASH) as client:
                historys = await client.get_messages(
                    int(self.group_id),
                    limit=100,
                    filter=InputMessagesFilterPhotos,
                    offset_id=offset_id)
                print(f'{historys=}')
                if historys == []:
                    break
                for history in historys:
                    file = history.media.photo.__dir__()
                    print(f'{file=}')
                    all_messages.append(
                        await client.download_media(
                            history,
                            file='media/temp/img'))

                    print(f'{all_messages[-1]=}')

                offset_id = historys[len(historys) - 1].id
        print('Здесь')
        return all_messages
