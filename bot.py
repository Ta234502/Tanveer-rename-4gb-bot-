from pyrogram import Client, idle
from config import *
import pyrogram.utils

pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -100999999999999

bot = Client(
    "Renamer",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)

# Only run bot (safe)
bot.start()
print("Bot Started 🔥")
idle()
bot.stop()




# Tanveer Developer 
# Please Don't Remove Credit 🥺
# Telegram Channel @TVR_BOTS
# Developer @SONY_YAY_0000 & @T4NVEER_HERE
