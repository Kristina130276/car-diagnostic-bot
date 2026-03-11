import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
שלום 👋
אני בוט לאבחון תקלות ברכב.

שלחו:
• צילום של לוח המחוונים
או
• קוד תקלה (לדוגמה: U3000)

ואנסה להסביר מה התקלה.
"""
    await update.message.reply_text(text)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "קיבלתי את התמונה 📷\n\nבגרסה הבאה אנסה לזהות את התקלה מהצילום."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.upper()

    if "U3000" in code:
        response = """
קוד תקלה: U3000

משמעות אפשרית:
תקלה במודול בקרת ABS או בעיית תקשורת במערכת.

מה לבדוק:
• מתח מצבר
• חיבורים למודול ABS
• חיישני גלגל
"""
    else:
        response = "קיבלתי את הקוד. בהמשך אחפש אותו במסד הנתונים."

    await update.message.reply_text(response)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
app.add_handler(MessageHandler(filters.TEXT, handle_text))

app.run_polling(close_loop=False)
import time
while True:
    time.sleep(10)
