import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import ephem

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

def greet_user(update, context):
    logger.info('Вызван /start')
    update.message.reply_text('Здарова')

def talk_to_me(update, context):
    text = update.message.text
    logger.info(text)
    update.message.reply_text(text)

def astronomy(update, context):
    text = update.message.text
    args = text.split()
    planet_name = args[1]
    if planet_name == 'Mars':
        planet = ephem.Mars('2023/02/17')
        
    elif planet_name == 'Pluto':
          planet = ephem.Pluto('2023/02/17')

    else:
         update.message.reply_text('Других планет я не знаю')   
         return

    planet = ephem.constellation(planet)
    logger.info('Вызван /planet')
    update.message.reply_text(planet)
    
def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', astronomy))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')

    mybot.start_polling()
    mybot.idle()
    
if __name__ == '__main__':
    main()
    