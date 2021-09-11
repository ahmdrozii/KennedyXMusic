# Module by https://github.com/tofikdn
# Copyright (C) 2021 TdMusic

import requests
from config import BOT_USERNAME
from pyrogram import Client
from helpers.filters import command


@Client.on_message(command(["lirik", f"lirik@{BOT_USERNAME}"]))
async def lirik(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**/lirik (masukkan judul lagu)**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("**processing...**")
        resp = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("**Lirik tidak ditemukan!**, masukkan judul lagu dengan lebih jelas.")
