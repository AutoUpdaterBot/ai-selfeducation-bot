import logging
from telegram.ext import Application

# Настройка логов
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def post_init(app: Application):
    logging.info("Бот успешно инициализирован")

if __name__ == "__main__":
    try:
        app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).post_init(post_init).build()
        app.add_handler(CommandHandler("start", start))
        logging.info("Запуск бота...")
        app.run_polling()
    except Exception as e:
        logging.critical(f"FATAL ERROR: {str(e)}")
        sys.exit(100)
