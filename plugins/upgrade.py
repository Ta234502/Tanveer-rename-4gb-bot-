from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters


# 🔘 Callback Button Upgrade
@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):

    text = """<b>💰 Upgrade Plans</b>

<b>🆓 Free Plan</b>
➜ Daily Upload Limit: 2GB
➜ Price: ₹0

<b>🪙 Basic</b>
➜ Daily Upload Limit: 20GB
➜ Price: ₹49 / $0.59 per month

<b>⚡ Standard</b>
➜ Daily Upload Limit: 50GB
➜ Price: ₹99 / $1.19 per month

<b>💎 Pro</b>
➜ Daily Upload Limit: 100GB
➜ Price: ₹179 / $2.16 per month

<b>💳 Payment Process</b>

➜ Plan lene ke liye niche button pe click karo  
➜ Admin ko DM karo  
➜ Waha tumhe UPI / QR diya jayega  
➜ Payment ke baad screenshot bhejna hoga  

⚠️ Payment details bot me nahi dikhayi jaati (security reasons)

<b>📩 Contact Admin:</b> @SONY_YAY_0000
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💬 Contact Admin", url="https://t.me/SONY_YAY_0000"),
            InlineKeyboardButton("❌ Cancel", callback_data="cancel")
        ]
    ])

    await update.message.edit_text(
        text=text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )


# 🔘 Command /upgrade
@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):

    text = """<b>💰 Upgrade Plans</b>

<b>🆓 Free Plan</b>
➜ Daily Upload Limit: 2GB
➜ Price: ₹0

<b>🪙 Basic</b>
➜ Daily Upload Limit: 20GB
➜ Price: ₹49 / $0.59 per month

<b>⚡ Standard</b>
➜ Daily Upload Limit: 50GB
➜ Price: ₹99 / $1.19 per month

<b>💎 Pro</b>
➜ Daily Upload Limit: 100GB
➜ Price: ₹179 / $2.16 per month

<b>💳 Payment Process</b>

➜ Plan lene ke liye niche button pe click karo  
➜ Admin ko DM karo  
➜ Waha tumhe UPI / QR diya jayega  
➜ Payment ke baad screenshot bhejna hoga  

⚠️ Payment details bot me nahi dikhayi jaati (security reasons)

<b>📩 Contact Admin:</b> @SONY_YAY_0000
"""

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💬 Contact Admin", url="https://t.me/SONY_YAY_0000"),
            InlineKeyboardButton("❌ Cancel", callback_data="cancel")
        ]
    ])

    await message.reply_text(
        text=text,
        reply_markup=keyboard,
        quote=True,
        disable_web_page_preview=True
    )


# Tanveer Developer 
# Please Don't Remove Credit 🥺
# Telegram Channel @TVR_BOTS
# Developer @SONY_YAY_0000 & @T4NVEER_HERE