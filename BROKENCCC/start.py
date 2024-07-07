from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['/start']]
    update.message.reply_text(
        'Hi! I M CC Checker Bot By @Mrbrokn \n**Send me card details in the format**::\nnumber, exp_month, exp_year, cvc',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
