from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from app.utils.file_utils import file_reader

TAMPLATES_DIR = "app/templates"

async def start_callback(update:Update, context:ContextTypes.DEFAULT_TYPE):

    keyboard_buttons = [
        [InlineKeyboardButton("Ctan", callback_data = "auto_ctan"),
         ]
    ]

    keyboard_markup = InlineKeyboardMarkup(keyboard_buttons)

    response:str = file_reader(TAMPLATES_DIR, "start_command.md")
    
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = response,
        reply_markup = keyboard_markup,
        parse_mode = 'HTML'
    )

# async def about_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
#     head = "Bot idealizado e criado pelos alunos da computação:\n......\nSeu intuito é o de facilitar a visualização dos cardápios." 
#     obs = '\n \U0000203C >*OBS:* O bot não se encontra em sua versão final ainda sofrerá bastantes alterações.'
    
#     await update.message.reply_text(head + obs, parse_mode='Markdown')

async def about_callback(update:Update, context:ContextTypes.DEFAULT_TYPE):
    pass

async def help_callback(update:Update, context:ContextTypes.DEFAULT_TYPE):
    
    response:str = file_reader(TAMPLATES_DIR, "help_command.md")
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=response,
        reply_to_message_id=update.message.message_id,
        parse_mode='HTML'
    )