from telethon import TelegramClient
from telethon.tl.types import PeerChannel
import _credentials


api_id   = _credentials.api_id
api_hash = _credentials.api_hash


client = TelegramClient('anonyyyyyyyyy1', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    # print(me.stringify())
    my_channel = await client.get_entity(PeerChannel(-1001861730306))
    print(my_channel.stringify())

with client:
	client.loop.run_until_complete(main())



