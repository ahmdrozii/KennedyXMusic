from time import time
from datetime import datetime
from config import BOT_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["p", f"p@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await m_reply.edit_text(
        f"`{delta_ping * 1000:.3f} ms`"
    )
