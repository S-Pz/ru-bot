from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters,  CallbackQueryHandler, Defaults
from zoneinfo import ZoneInfo

from app.handlers.common_handlers import start_callback, about_callback, help_callback
from app.handlers.lunch_menu_handlers import lunch_buttons_callback, lunch_menus_callback
from app.handlers.automatic_handlers import automatic_message_callback
class Bot:
    
    def __init__(self, token:str, username:str):
        self.token = token
        self.bot_username = username
        self.app = Application.builder().token(token).defaults(Defaults(tzinfo=ZoneInfo("America/Sao_Paulo"))).build()

    def common_handlers(self):
        self.app.add_handler(CommandHandler('start', start_callback))
        self.app.add_handler(CallbackQueryHandler(automatic_message_callback, pattern = "^auto_"))
        self.app.add_handler(CommandHandler('sobre', about_callback))
        self.app.add_handler(CommandHandler('ajuda', help_callback))
    
    def lunch_handlers(self):
        self.app.add_handler(CommandHandler("almoco", lunch_buttons_callback))
        self.app.add_handler(CallbackQueryHandler(lunch_menus_callback, pattern = "^lunch_"))
    
    def run(self):
        self.app.run_polling(poll_interval = 4)