import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

async def start(update: Update, context):
    await update.message.reply_text("Привет! Я твой помощник в саморазвитии. Напиши /help для списка команд")

async def help_command(update: Update, context):
    help_text = """
    Доступные команды:
    /start - начать работу
    /task - получить задание
    /motivate - мотивационное сообщение
    """
    await update.message.reply_text(help_text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()
