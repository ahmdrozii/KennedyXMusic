from pyrogram import Client
import asyncio
from config import SUDO_USERS, PMPERMIT, OWNER_NAME, BOT_USERNAME, BOT_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from pyrogram import filters
from pyrogram.types import Message
from callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
            f"⚠️ Pesan otomatis dari **[{BOT_NAME}](https://t me/{BOT_USERNAME}).\n\n∅ Catatan:**\n» Jangan spam agar bot tidak lag.\n» Jangan memasukkan antrian lagu terlalu banyak.\n\nJoin ke @{GROUP_SUPPORT} untuk keluhan mengenai bot atau hubungi @{OWNER_NAME}\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("✅ pmpermit turned on")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("❌ pmpermit turned off")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("approved to pm due to outgoing messages")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("y", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("approved to pm.")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("n", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("disapproved to pm.")
        return
    message.continue_propagation()
