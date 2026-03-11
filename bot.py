import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "שלום 👋\n"
        "אני בוט לאבחון תקלות ברכב.\n\n"
        "שלחו צילום של לוח המחוונים או קוד תקלה."
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "U3000" in text.upper():
        await update.message.reply_text(
            "קוד תקלה: U3000\n\n"
            "משמעות אפשרית:\n"
            "תקלה במודול ABS או בעיית תקשורת.\n\n"
            "מה לבדוק:\n"
            "• מתח מצבר\n"
            "• חיבורים למודול ABS\n"
            "• חיישני גלגל"
        )
    else:
        await update.message.reply_text(f"קיבלתי: {text}")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("קיבלתי את התמונה 📷")

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is missing")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("Bot is starting...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
