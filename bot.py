import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger=logging.getLogger(__name__)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user=update.effective_user
    await update.message.reply_html(rf"Hi {user.mention_html()}!",reply_markup=ForceReply(selective=True),)

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user=update.effective_user
    print(user)
    await update.message.reply_html(rf"Goodbye {user.username}!",reply_markup=ForceReply(selective=True),)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    if update.message.text == "hi" : 
        await update.message.reply_text( "Hello Buddy")    
    else: 
        await update.message.reply_text( "wrong question")
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact=update.effective_user
    print(contact)
    await update.message.reply_text(f"your number is {contact}")
async def price_btc(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    # await update.message.reply_text(f"the BTC price is  {} ")
    await None
def main()->None:
    """Start the bot."""
    application=Application.builder().token("Token").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("end", end))
    application.add_handler(CommandHandler("num", contact_handler))
    application.add_handler(CommandHandler("price_btc", contact_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
if __name__ == "__main__":
    main()