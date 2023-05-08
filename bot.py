import telegram, logging, functions, dotenv, os
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
from telegram import Update, MessageEntity
from tgvmax.py import Monitor


#Configure a logs template
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load environment variables
dotenv.load_dotenv()

# Récupérer la valeur de la variable d'environnement TOKEN
TOKEN = os.environ.get('TOKEN')



if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', functions.start) 
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), functions.echo)
    unknown_handler = MessageHandler(filters.COMMAND, functions.unknown)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)

    application.run_polling()

    monitor = Monitor()
    while true:
        for research in Monitor().listResearch:
            i
        application.bot.send_message(PRIVATECHATID, "Nouveau train disponible !\n
                                    Date : " + result.date + "\n
                                    Départ : " + result.origine + "\n
                                    Destination : " + result.destination)


   
