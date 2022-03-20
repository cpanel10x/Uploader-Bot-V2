

import asyncio
from pyrogram import types, errors
from plugins.config import Config
from plugins.database.database import db

async def OpenSettings(m: "types.Message"):
    usr_id = m.chat.id
    user_data = await db.get_user_data(usr_id)
    if not user_data:
        await m.edit("Failed to fetch your data from database!")
        return
    upload_as_doc = user_data.get("upload_as_doc", False)
   
    thumbnail = user_data.get("thumbnail", None)
    #generate_sample_video = user_data.get("generate_sample_video", False)
    generate_ss = user_data.get("generate_ss", False)
    buttons_markup = [
        [types.InlineKeyboardButton(f"Gửi dạng {'🎥 Video' if upload_as_doc else '🗃️ File'}",
                                    callback_data="triggerUploadMode")],
        #[types.InlineKeyboardButton(f"Generate Sample Video {'✅' if generate_sample_video else '❌'}", 
                                    #callback_data="triggerGenSample")],
        [types.InlineKeyboardButton(f"🖼️ Xem ảnh chụp video {'✅' if generate_ss else '✖️'}", 
                                    callback_data="triggerGenSS")],
        [types.InlineKeyboardButton(f"{'Thay' if thumbnail else '🌃 Đặt'} ảnh bìa",
                                    callback_data="setThumbnail")]
    ]
    if thumbnail:
        buttons_markup.append([types.InlineKeyboardButton("🌆 Xem ảnh bìa",
                                                          callback_data="showThumbnail")])
    buttons_markup.append([types.InlineKeyboardButton("♨️ ᴄʟᴏsᴇ",
                                                      callback_data="close")])

    try:
        await m.edit(
            text="**Cài đặt cấu hình tại đây**",
            reply_markup=types.InlineKeyboardMarkup(buttons_markup),
            disable_web_page_preview=True,
            parse_mode="Markdown"
        )
    except errors.MessageNotModified: pass
    except errors.FloodWait as e:
        await asyncio.sleep(e.x)
        await show_settings(m)
    except Exception as err:
        Config.LOGGER.getLogger(__name__).error(err)

