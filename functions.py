import logging, pyqrcode
from telegram import Update
from telegram.ext import ContextTypes

# Set up logging
logger = logging.getLogger(__name__)

ASKQRCODE, CONVERTURL = range(2)

# Fonction qui sera appelée lors de la commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
            chat_id=update.efféctive_chat.id, 
            text='Bonjour! Je suis un bot Telegram!'
            )


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
    
