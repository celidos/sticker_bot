import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')

from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import Update


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Echo the user message."""
    # await update.message.reply_sticker("https://github.com/TelegramBots/book/raw/master/src/docs/sticker-fred.webp")
    await update.message.reply_sticker("CAACAgQAAxkBAAEbPlZjo9b3kw66yPRozJQNV-DnBihVIQACAgEAAsr2HwABrzgUM6oS3UEsBA")


    # await update.message.reply_text(update.message.text)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()