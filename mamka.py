import asyncio
import requests
import random
import json
from time import sleep
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, MessageMediaDocument, PeerChannel, MessageMediaPhoto, InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest

api_id = 14650309
api_hash = '7e2674c11da3743d051ed9e9b848bd11'

client = TelegramClient('data', api_id, api_hash, device_model="Iphone", system_version="6.12.0",
                        app_version="10 P (28)")

client.start()

chat = input("https://t.me/evpachat")

@client.on(events.NewMessage(chats = chat))
async def handler(event):
    with open('base.json', 'r', encoding='UTF-8') as t:
        text = json.load(t)
        i = random.choice(text['curses'])
    await event.reply(i)
    await asyncio.sleep(2)



client.run_until_disconnected()
