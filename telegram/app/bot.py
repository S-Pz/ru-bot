from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
from app.handlers.common_handlers import start_callback, about_callback, help_callback

class Bot:
    
    def __init__(self, token:str, username:str):
        self.token = token
        self.bot_username = username
        self.app = Application.builder().token(token).build()

    def common_handlers(self):
        self.app.add_handler(CommandHandler('start', start_callback))
        self.app.add_handler(CommandHandler('sobre', about_callback))
        self.app.add_handler(CommandHandler('ajuda', help_callback))
    
    def job_queue_test(self):
        self.app.job_queue
        #job_queue.run_repeating(help_callback, interval= 2)
    def run(self):
        self.app.run_polling(poll_interval = 4)