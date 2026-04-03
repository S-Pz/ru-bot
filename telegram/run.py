import os
from app.bot import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')

def main():
    
    if not BOT_TOKEN:
        raise ValueError("ERRO: BOT_TOKEN, não encontrada no arquivo .env")
    
    bot_app = Bot(BOT_TOKEN, BOT_USERNAME)
    
    bot_app.common_handlers()
    bot_app.job_queue_test()
    bot_app.run()

if __name__ == '__main__':
    main()