# Copyright (C) 2021 By KennedyProject


import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as kennedy
from config import SUDO_USERS

@Client.on_message(filters.command(["bc"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`starting broadcast...`")
        if not message.reply_to_message:
            await wtf.edit("processing...")
            return
        lmao = message.reply_to_message.text
        async for dialog in kennedy.iter_dialogs():
            try:
                await kennedy.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`broadcasting...`\nsent to `{sent}` chats, failed in {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`gcast succesfully`\nsent to `{sent}` chats, failed in {failed} chats")
