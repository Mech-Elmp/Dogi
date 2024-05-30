from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import Config
from helper.database import db

async def not_subscribed(_, client, message):
    await db.add_user(client, message)
    if not Config.FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id) 
        if user.status in {enums.ChatMemberStatus.BANNED, enums.ChatMemberStatus.LEFT}:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ  ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{Config.FORCE_SUB}") ]]
    text = "**ʙᴏᴛ  ɪs  ᴀᴄᴛɪᴠᴇ  ʙᴜᴛ  ᴏɴʟʏ  ᴏᴜʀ  ᴄʜᴀɴɴᴇʟ  ᴍᴇᴍʙᴇʀs  ᴄᴀɴ  ᴜsᴇ  ᴛʜɪs  ʙᴏᴛ \n\nᴄʟɪᴄᴋ  ʙᴇʟᴏᴡ  ᴊᴏɪɴ  ᴀɴᴅ  sᴇɴᴅ  ғɪʟᴇ  ᴀɢᴀɪɴ**"
    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="**ʏᴏᴜ  ᴀʀᴇ  ʙᴀɴɴᴇᴅ  ᴛᴏ  ᴜsᴇ  ᴍᴇ**")  
        elif user.status == enums.ChatMemberStatus.LEFT:
            return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          


