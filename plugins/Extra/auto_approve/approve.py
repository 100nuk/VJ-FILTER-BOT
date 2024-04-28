from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from info import AUTO_APPROVE_MODE

@Client.on_chat_join_request((filters.group | filters.channel))
async def auto_approve(client, message: ChatJoinRequest):
    if AUTO_APPROVE_MODE == True:
        chat = message.chat 
        user = message.from_user  
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        text = f"<b>ʜᴇʟʟᴏ {message.from_user.mention} 👋,\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {message.chat.title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>"
        await client.send_message(chat_id=user.id, text=text)
