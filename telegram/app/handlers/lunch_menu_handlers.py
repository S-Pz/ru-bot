import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from app.hooks.ctan_hook import date_and_horario_ctan

async def lunch_daily_ctan_callback(context:ContextTypes.DEFAULT_TYPE):

    today_date:str = datetime.datetime.now().strftime("%Y-%m-%d")
    
    response = date_and_horario_ctan("almoco", today_date)
    
    await context.bot.send_message(
        chat_id = context.job.chat_id,
        text = response,
        parse_mode = 'Markdown'
    )

async def lunch_buttons_callback(update:Update, context:ContextTypes.DEFAULT_TYPE):

    keyboard_buttons = [
        [InlineKeyboardButton("Ctan", callback_data = "lunch_ctan")]
    ]
    
    keyboard_markup = InlineKeyboardMarkup(keyboard_buttons)
    
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = "Qual ru deseja consultar ? \U0001F914",
        reply_markup = keyboard_markup
    )

async def lunch_menus_callback(update:Update, context:ContextTypes.DEFAULT_TYPE):
    
    callback_query:str = update.callback_query.data
    date:str = update.callback_query.message.date.strftime("%Y-%m-%d")
    
    if (callback_query == "lunch_ctan"):
        response = date_and_horario_ctan("almoco", date)
        
        await context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = response,
            parse_mode = 'Markdown'
        )
    