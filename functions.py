import logging
import os
import pyqrcode

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ContextTypes,
    CallbackContext, ConversationHandler
)

# Set up logging
logger = logging.getLogger(__name__)

QRCODE_START, QRCODE_END = range(2)


# Fonction qui sera appelée lors de la commande /start
async def start(update: Update, context: CallbackContext) -> None:
    logger.info("User %s started the conversation.", update.message.from_user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("Generate QR code", callback_data='qrcode')
        ],
        [
            InlineKeyboardButton("empty", callback_data='2')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose command', reply_markup=reply_markup)


# Fonction qui sera appelée lors de l'envoi d'un message texte
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text=update.message.text
            )


# Fonction qui sera appelée lorsqu'une commande inconnue est envoyée
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


async def ask_qrcode_url(update: Update, context: CallbackContext):
    try:
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='Veuillez entrer un URL à convertir en QR code'
                )
        return QRCODE_START
    except Exception as e:
        logger.exception("Error occurred whith the method ask_qrcode_url: %s", str(e))
        await context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred whith your URL.")


async def get_qrcode(update: Update, context: CallbackContext):
    try:
        url = pyqrcode.create(update.message.text)
        url.png('qrcode.png', scale=15)
        await context.bot.send_chat_action(update.message.chat.id, 'upload_document')
        await context.bot.send_document(update.message.chat.id, open('qrcode.png', 'rb'))
        os.remove("qrcode.png")
        return QRCODE_END
    except Exception as e:
        logger.exception("Error occurred while generating QR code: %s", str(e))
        await context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred while generating the QR code.")


# Definition de la fonction asynchrone de gestion du message contenant l'entrée texte de l'utilisateur
async def error(update: Update, context: CallbackContext) -> None:
    print(f'Update {update} cause error {context.error}')
    logging.exception("ERROR")


async def cancel(update, context) -> int:
    context.user_data.clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Opération annulée.")
    return ConversationHandler.END


async def handle_callback_query(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer() # Répondre au callback pour éviter une erreur de timeout
    #await query.edit_message_text(text="Selected option: {}".format(query.data))
    if query.data == "qrcode":
        await ask_qrcode_url(update, context)
    return ConversationHandler.END

