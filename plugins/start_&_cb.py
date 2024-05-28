"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/DigitalBotz/Digital-Rename-Bot/blob/main/LICENSE
"""

import random, asyncio, datetime, pytz, time, psutil, shutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, rkn
from helper.utils import humanbytes

upgrade_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('buy premium ✓', user_id=int(6705898491)),
         ],[
        InlineKeyboardButton("Bᴀᴄᴋ", callback_data = "start")
         ]])

upgrade_trial_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('buy premium ✓', user_id=int(6705898491)),
         ],[
        InlineKeyboardButton("ᴛʀɪᴀʟ - 𝟷𝟸 ʜᴏᴜʀs ✓", callback_data = "give_trial"),
        InlineKeyboardButton("Bᴀᴄᴋ", callback_data = "start")
         ]])

start_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('Uᴩᴅᴀ𝚃ᴇꜱ', url='https://t.me/Digital_Botz'),
        InlineKeyboardButton('Sᴜᴩᴩᴏʀ𝚃', url='https://t.me/DigitalBotz_Support')
        ],[
        InlineKeyboardButton('Aʙᴏυᴛ', callback_data='about'),
        InlineKeyboardButton('Hᴇʟᴩ', callback_data='help')
        ],[
        InlineKeyboardButton('💸 ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ 💸', callback_data='upgrade')
         ]])

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message) 
    if Config.RKN_PIC:
        await message.reply_photo(Config.RKN_PIC, caption=rkn.START_TXT.format(user.mention), reply_markup=start_button)       
    else:
        await message.reply_text(text=rkn.START_TXT.format(user.mention), reply_markup=start_button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("myplan"))
async def myplan(client, message):
    user_id  = message.from_user.id
    user = message.from_user.mention
    if await db.has_premium_access(user_id):
        
        data = await db.get_user(user_id)
        expiry_str_in_ist = data.get("expiry_time")
        time_left_str = expiry_str_in_ist - datetime.datetime.now()
       # time_left_str = await db.checking_remaining_time(user_id)
        #expiry_str_in_ist = time_left_str + datetime.datetime.now()
        
        await message.reply_text(f"⚜️ ʏᴏᴜʀ ᴘʟᴀɴs ᴅᴇᴛᴀɪʟs ᴀʀᴇ :\n\n👤 ᴜꜱᴇʀ : {user}\n⚡ ᴜꜱᴇʀ ɪᴅ : <code>{user_id}</code>\n⏰ ᴛɪᴍᴇ ʟᴇꜰᴛ : {time_left_str}\n⌛️ ᴇxᴘɪʀʏ ᴅᴀᴛᴇ : {expiry_str_in_ist}")
    else:
        m=await message.reply_sticker("CAACAgIAAxkBAAIBTGVjQbHuhOiboQsDm35brLGyLQ28AAJ-GgACglXYSXgCrotQHjibHgQ")
        await message.reply_text(f"ʜᴇʏ {user},\n\nʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴀɴʏ ᴀᴄᴛɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs, ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ 👇",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💸 ᴄʜᴇᴄᴋᴏᴜᴛ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ 💸", callback_data='upgrade')]]))			 
        await asyncio.sleep(2)
        await m.delete()

@Client.on_message(filters.private & filters.command("plans"))
import random, asyncio, datetime, pytz, time, psutil, shutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from helper.database import db
from config import Config, rkn
from helper.utils import humanbytes

# Inline keyboard buttons
upgrade_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('Buy Premium ✓', callback_data='buy_premium')],
    [InlineKeyboardButton("Back", callback_data="start")]
])

upgrade_trial_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('Buy Premium ✓', callback_data='buy_premium')],
    [InlineKeyboardButton("Trial - 12 Hours ✓", callback_data="give_trial")],
    [InlineKeyboardButton("Back", callback_data="start")]
])

start_button = InlineKeyboardMarkup([
    [InlineKeyboardButton('Updates', url='https://t.me/Digital_Botz'),
     InlineKeyboardButton('Support', url='https://t.me/DigitalBotz_Support')],
    [InlineKeyboardButton('About', callback_data='about'),
     InlineKeyboardButton('Help', callback_data='help')],
    [InlineKeyboardButton('💸 Upgrade to Premium 💸', callback_data='upgrade')]
])

# Start command handler
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message) 
    if Config.RKN_PIC:
        await message.reply_photo(Config.RKN_PIC, caption=rkn.START_TXT.format(user.mention), reply_markup=start_button)       
    else:
        await message.reply_text(text=rkn.START_TXT.format(user.mention), reply_markup=start_button, disable_web_page_preview=True)

# Myplan command handler
@Client.on_message(filters.private & filters.command("myplan"))
async def myplan(client, message):
    user_id  = message.from_user.id
    user = message.from_user.mention
    if await db.has_premium_access(user_id):
        data = await db.get_user(user_id)
        expiry_time = data.get("expiry_time")
        expiry_str_in_ist = datetime.datetime.strptime(expiry_time, "%Y-%m-%d %H:%M:%S")
        time_left_str = expiry_str_in_ist - datetime.datetime.now()
        await message.reply_text(f"⚜️ Your plan details are:\n\n👤 User: {user}\n⚡ User ID: <code>{user_id}</code>\n⏰ Time Left: {time_left_str}\n⌛️ Expiry Date: {expiry_str_in_ist}")
    else:
        m = await message.reply_sticker("CAACAgIAAxkBAAIBTGVjQbHuhOiboQsDm35brLGyLQ28AAJ-GgACglXYSXgCrotQHjibHgQ")
        await message.reply_text(
            f"Hey {user},\n\nYou do not have any active premium plans. If you want to take premium then click on the below button 👇",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💸 Checkout Premium Plans 💸", callback_data='upgrade')]]))			 
        await asyncio.sleep(2)
        await m.delete()

# Plans command handler
@Client.on_message(filters.private & filters.command("plans"))
async def plans(client, message):
    user = message.from_user
    free_trial_status = await db.get_free_trial_status(user.id)
    if not await db.has_premium_access(user.id):
        if not free_trial_status:
            await message.reply_text(text=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_trial_button, disable_web_page_preview=True)
        else:
            await message.reply_text(text=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button, disable_web_page_preview=True)
    else:
        await message.reply_text(text=rkn.UPGRADE.format(user.mention), reply_markup=upgrade_button, disable_web_page_preview=True)

# Callback query handler
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=rkn.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=start_button)
        
    elif data == "help":
        await query.message.edit_text(
            text=rkn.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Thumbnail", callback_data="thumbnail"),
                InlineKeyboardButton("Caption", callback_data="caption")
                ],[          
                InlineKeyboardButton("Custom File Name", callback_data="custom_file_name")    
                ],[          
                InlineKeyboardButton("About", callback_data="about"),
                InlineKeyboardButton("Metadata", callback_data="digital_meta_data")
                ],[
                InlineKeyboardButton("Back", callback_data="start")
                  ]]))         
        
    elif data == "about":
        await query.message.edit_text(
            text=rkn.ABOUT_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Source", callback_data="source_code"),
                InlineKeyboardButton("Bot Status", callback_data="bot_status")
                ],[
                InlineKeyboardButton("Live Status", callback_data="live_status"),
                InlineKeyboardButton("Upgrade", callback_data="upgrade")
                ],[   
                InlineKeyboardButton("Back", callback_data="start")
                ]]))    
        
    elif data == "upgrade":
        free_trial_status = await db.get_free_trial_status(query.from_user.id)
        if not await db.has_premium_access(query.from_user.id):
            if not free_trial_status:
                await query.message.edit_text(text=rkn.UPGRADE, disable_web_page_preview=True, reply_markup=upgrade_trial_button)   
            else:
                await query.message.edit_text(text=rkn.UPGRADE, disable_web_page_preview=True, reply_markup=upgrade_button)
        else:
            await query.message.edit_text(text=rkn.UPGRADE, disable_web_page_preview=True, reply_markup=upgrade_button)
           
    elif data == "give_trial":
        await query.message.delete()
        free_trial_status = await db.get_free_trial_status(query.from_user.id)
        if not free_trial_status:            
            await db.give_free_trail(query.from_user.id)
            new_text = "**Your premium trial has been added for 12 hours.\n\nYou can use free trial for 12 hours from now 😀\n\nआप अब से 12 घंटे के लिए निःशुल्क ट्रायल का उपयोग कर सकते हैं 😀**"
        else:
            new_text = "**🤣 You already used free trial. Now no more free trial. Please buy subscription here 👉 /plans**"
        await client.send_message(query.from_user.id, text=new_text)

    elif data == "thumbnail":
        await query.message.edit_text(
            text=rkn.THUMBNAIL,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("Back", callback_data="help")]])) 
      
    elif data == "caption":
        await query.message.edit_text(
            text=rkn.CAPTION,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("Back", callback_data="help")]])) 
      
    elif data == "custom_file_name":
        await query.message.edit_text(
            text=rkn.CUSTOM_FILE_NAME,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("Back", callback_data="help")]])) 
      
    elif data == "digital_meta_data":
        await query.message.edit_text(
            text=rkn.DIGITAL_METADATA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("Back", callback_data="help")]])) 
      
    elif data == "bot_status":
        total_users = await db.total_users_count()
        total_premium_users = await db.total_premium_users_count()
        uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        sent = humanbytes(psutil.net_io_counters().bytes_sent)
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        await query.message.edit_text(
            text=rkn.BOT_STATUS.format(uptime, total_users, total_premium_users, sent, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("Back", callback_data="about")]])) 
      
    elif data == "live_status":
        currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
        total, used, free = shutil.disk_usage(".")
        total = humanbytes(total)
        used = humanbytes(used)
        free = humanbytes(free)
        sent = humanbytes(psutil.net_io_counters().bytes_sent)
        recv = humanbytes(psutil.net_io_counters().bytes_recv)
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        await query.message.edit_text(
            text=rkn.LIVE_STATUS.format(currentTime, cpu_usage, ram_usage, total, used, disk_usage, free, sent, recv),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("Back", callback_data="about")]])) 
      
    elif data == "source_code":
        await query.message.edit_text(
            text=rkn.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
           #Whoever is deploying this repo is given a warning ⚠️ not to remove this repo link #first & last warning ⚠️   
                InlineKeyboardButton("💞 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 💞", url="https://github.com/DigitalBotz/Digital-Rename-Bot")
            ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                 ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
