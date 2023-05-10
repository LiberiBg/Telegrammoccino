import dotenv
import functions
import logging
import os

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    filters,
    MessageHandler,
    ConversationHandler, CallbackQueryHandler
)

#Configure a logs template
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load environment variables
dotenv.load_dotenv()

# Récupérer la valeur de la variable d'environnement TOKEN
TOKEN = os.environ.get('TOKEN')

QRCODE_START, QRCODE_END = range(2)
if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).concurrent_updates(True).build()

    application.add_handler(CommandHandler('start', functions.start))
    application.add_handler(ConversationHandler(
        entry_points=[CommandHandler("qrcode", functions.ask_qrcode_url)],
        states={
            QRCODE_START: [MessageHandler(filters.TEXT & ~filters.COMMAND, functions.get_qrcode)],
            QRCODE_END: [MessageHandler(filters.TEXT & ~filters.COMMAND, functions.get_qrcode)],
        },
        fallbacks=[CommandHandler("cancel", functions.cancel)],
        allow_reentry=True,
        name='Conversation generate qrcode from url'
    ))
    application.add_handler(CallbackQueryHandler(functions.handle_callback_query))
    #application.add_error_handler(functions.error)
    #application.add_handler(MessageHandler(filters.COMMAND, functions.unknown))

    print("Bot's polling...")
    application.run_polling()
