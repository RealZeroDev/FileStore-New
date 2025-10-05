import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = "5010"

# Owner / Admins
OWNER_ID = 6819408964
ADMINS = [957204779, 8034171951]

# Telegram API / Bot
SESSION = "RealZeroking"  # if you have StringSession, replace here
TOKEN = "8386375283:AAGLjs20CWgq8AwkYTAo3-iRiS9j9SpkBTI"
API_ID = 28449420
API_HASH = "608b71c13cec20da6662327fa1fc7d35"
WORKERS = 5

# Mongo Database
DB_URI = "mongodb+srv://thezerodev:GtiCjva8tQnD1PRN@cluster0.t9gtmbv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "thezerodev"

# Channels
FSUBS = [[-1002633749982, True, 10]]  # [channel_id, request_enabled, timer_in_minutes]
DB_CHANNEL = -1002861366260  # Primary FileStore Channel (without quotes)

# Auto Delete
AUTO_DEL = 300

# Shortlink Settings
SHORT_URL = "arolinks.com"
SHORT_API = "9fcfb5aef7643e1859aa886defb44a34fc5ed096"
SHORT_TUT = "https://t.me/How_to_Download_7x/26"

# Extra Settings
MSG_EFFECT = 5046509860389126442
DISABLE_BTN = True
PROTECT = True

# Messages Configuration
MESSAGES = {
    "START": "START": "<b>›› ʜᴇʏ!!, {first} ~ 🎬\n\nʟᴏᴠᴇ ᴍᴏᴠɪᴇs & ᴡᴇʙsᴇʀɪᴇs? 🍿\nɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ғɪɴᴅ ᴀʟʟ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴄᴏɴᴛᴇɴᴛ ғᴀsᴛ & ᴇᴀsʏ ✅</b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b>›››› ғᴏʀ ᴍᴏʀᴇ: @ZeroNetOfficial 
 ›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: Cʟɪᴄᴋ ʜᴇʀᴇ 
›› ᴏᴡɴᴇʀ: @RealZeroKing
›› ʟᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3 
›› ʟɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ ᴠ2 
›› ᴅᴀᴛᴀʙᴀsᴇ: Mᴏɴɢᴏ ᴅʙ 
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @RealZeroKing</b></blockquote>",
    "REPLY": "<b>For More Join - @ZeroNetOfficial</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
