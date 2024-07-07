import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from bot import TELEGRAM_BOT_TOKEN, start, check_card_from_message, check_card_from_file

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command handler
def start_command(update: Update, context: CallbackContext) -> None:
    start(update, context)


def check_card_command(update: Update, context: CallbackContext) -> None:
    if context.args:
        result = check_card_from_message(context.args[0])
    else:
        result = 'Usage: /chk number,exp_month,exp_year,cvc'
    
    update.message.reply_text(result)

# Check card from file command handler
def check_card_file_command(update: Update, context: CallbackContext) -> None:
    file_path = 'cc.txt'  
    result = check_card_from_file(file_path)
    update.message.reply_text(result)

# Error handler
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("chk", check_card_command))
    dispatcher.add_handler(CommandHandler("chkfile", check_card_file_command))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
