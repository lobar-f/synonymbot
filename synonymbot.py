import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Find synonym", callback_data='1'),
            InlineKeyboardButton("Show usage", callback_data='2'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Welcome to synonym bot! \n Please choose from the commands below :', reply_markup=reply_markup)

def add(update: Update) -> None:

    message_splited = update.message.text.split(' ')
    expense= " ".join(message_splited[1::])
    
    
    # if response.get('weather',None) !=None:
    #     update.message.reply_text(
    #         f'Today weather in {response["name"]}:\n\n{response["weather"][0]["main"].capitalize()}\n{response["weather"][0]["description"].capitalize()}')
    # else:
    #     update.message.reply_text(
    #         'City not found.')
    # answer = user_input.str()
    return expense

def new(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    
    update.message.reply_text(add(user_input))

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5575227199:AAHgtqoj4LFeyC_rXTQ32jO-2adb7XbxJ84")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('new', new))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
