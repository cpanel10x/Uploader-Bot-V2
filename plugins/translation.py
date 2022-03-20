from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
👋 Xin chào {} ♡

Bấm HELP để xem hướng dẫn sử dụng!
"""
    HELP_TEXT = """
GỬI LINK VIDEO

➠ Gửi liên kết cần tải VIDEO hoặc TẬP TIN

ĐẶT HÌNH BÌA

➠ Gửi hình bất kì để đặt làm ảnh bìa cho mọi video (tùy chọn)

XÓA HÌNH BÌA

➠ Gửi lệnh /delthumb để xóa hình bìa

CÀI ĐẶT

➠ Cài đặt cấu hình

XEM HÌNH BÌA

➠ Gửi /showthumb để xem hình bìa tùy chọn
 
"""
    ABOUT_TEXT = """
**LIÊN HỆ** : [ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ](http://t.me/cpanel10x)

**KÊNH : [DLCBOT](https://t.me/dlcvietnam)

"""


    PROGRESS = """
🔰 Tốc độ : {3}/s\n\n
🌀 Hoàn thành : {1}\n\n
🎥 Kích thước  : {2}\n\n
⏳ Thời gian còn lại : {4}\n\n
"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗜️ Cài đặt', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('❔ Hướng dẫn', callback_data='help'),
        InlineKeyboardButton('👨‍🚒 Thông tin', callback_data='about')
        ],[
        InlineKeyboardButton('ĐÓNG', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👨‍🚒 Thông tin', callback_data='about')
        ],[
        InlineKeyboardButton('ĐÓNG', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Hướng dẫn', callback_data='help')
        ],[
        InlineKeyboardButton('ĐÓNG', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ĐÓNG', callback_data='close')
        ]]
    )
    TEXT = "Gửi hình bất kì để làm ảnh bìa cho video"
    IFLONG_FILE_NAME = " Tên file chứa tối đa 64 ký tự. "
    RENAME_403_ERR = "Xin lỗi, bạn không có quyền đổi tên file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "Chọn định dạng hoặc kích thước 🗄️ để muốn tải"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_FILE = "📥 Đang tải "
    UPLOAD_FILE = " Đang upload 📤 \n\n lên transfer.sh "
    ANNO_UPLOAD = " Đang upload 📤 \n\n lên anonfiles.com "
    BAY_UPLOAD = " Đang upload 📤 \n\n lên bayfiles.com "
    GO_FILE_UPLOAD = " 📤Đang upload📤 \n\n lên gofile.io "
    DOWNLOAD_START = "Đang xử lí...⏳"
    UPLOAD_START = "📤 Đang gửi..."
    RCHD_BOT_API_LIMIT = "kích thước lớn hơn quy định (50MB). Đang thử lại."
    RCHD_TG_API_LIMIT = "Đã tải về trong {} giây.\nPhát hiện kích thước: {}\nXin lỗi, telegram chỉ cho phép file tối đa 2GB."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Hoàn tất"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Xử lí trong vòng {} giây.\n\nCảm ơn đã xử dụng\n\nHoàn tất gửi file sau {} giây"
    NOT_AUTH_USER_TEXT = "Vui lòng gõ /upgrade để nâng cấp."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Phát hiện kích thước: {}. Thành viên miễn phí bị giới hạn: {}\nVui lòng gõ /upgrade để nâng cấp.\nNếu đây là lỗi vui lòng liên hệ <a href='https://telegram.dog/cpanel10x'>@cpanel10x</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Đã lưu ảnh bìa tùy chọn."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Đã xóa ảnh bìa tùy chọn"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Không có ảnh bìa tùy chọn"
    NO_VOID_FORMAT_FOUND = "Lỗi... <code>{}</code>"
    FILE_NOT_FOUND = "Lỗi... Không tìm thấy file!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Có lỗi xảy ra, vui lòng thử lại.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    AFTER_GET_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n"
    AFTER_GET_DL_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\nValid for <b>14</b> days."
    #AFTER_GET_DL_LINK = " {} valid for 30 or more days.\n\n Join : @Tellybots_4u \n For the list of Telegram bots. "
    AFTER_GET_GOFILE_LINK = " <b>File Name :</b> <code>{}</code>\n<b>File Size :</b> {}\n<b>File MD5 Checksum :</b> <code>{}</code>\n\n<b>⚡Link⚡ :</b> <code>{}</code>\n\n Valid untill 10 days of inactivity\nJoin : @TGBotsCollection"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "Join : @TGBotsCollectionbot \n For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    CHECK_LINK = "Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ʟɪɴᴋ ⌛"

