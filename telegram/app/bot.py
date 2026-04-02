from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
from handlers.common_handlers import start_callback, about_callback, help_callback

class Bot:
    
    def _init_(self, token:str, username:str):
        self.token = token
        self.bot_username = username
        self.app = Application.builder().token(token).build()

    def common_handlers(self):
        self.app.add_handler('start', start_callback)
        self.app.add_handler('sobre', about_callback)
        self.app.add_handler('ajuda', help_callback)
        
    def run(self):
        self.app.run_pulling(poll_interval = 4)