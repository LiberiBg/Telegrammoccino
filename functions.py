import logging, pyqrcode
from telegram import (
        Update,
        InlineKeyboardButton,
        InlineKeyboardMarkup
        )
from telegram.ext import (
        ContextTypes,
        CallbackContext
        )

# Set up logging
logger = logging.getLogger(__name__)

ASKQRCODE, CONVERTURL = range(2)

# Fonction qui sera appelée lors de la commande /start
async def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Option 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Please choose:', reply_markup=reply_markup) 

# Fonction qui sera appelée lors de l'envoi d'un message texte
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=update.message.text
            )


# Fonction qui sera appelée lorsqu'une commande inconnue est envoyée
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


async def askQrCode(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Veuillez entrer un URL à convertir en QR code'
            )


async def convertUrl(update : Update, context : ContextTypes.DEFAULT_TYPE):
    url=pyqrcode.create(update.message.text)
    url.png('qrcode.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open('qrcode.png','rb' ))
