import os
import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from telegram.constants import ParseMode
from filter import lunch_filter, dinner_filter, response_format, response_format_2
from dotenv import load_dotenv


#Load file .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
BOT_USERNAME = os.getenv('BOT_USERNAME')

#commands
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    with open('../text_commands_files/start_command.md','r') as f:
        start:str = f.read()
    await update.message.reply_html(start)
    
async def about_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    head = "Bot idealizado e criado pelos alunos da computação:\n......\nSeu intuito é o de facilitar a visualização dos cardápios." 
    obs = '\n \U0000203C >*OBS:* O bot não se encontra em sua versão final ainda sofrerá bastantes alterações.'
    
    await update.message.reply_text(head + obs, parse_mode='Markdown')

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    with open('../text_commands_files/help_command.md','r') as f:
        help:str = f.read()
    await update.message.reply_html(help)

async def info_schedules(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    with open('../text_commands_files/info_schedules.md','r') as f:
        schedules:str = f.read()
    await update.message.reply_html(schedules)

async def info_price(update:Update, context: ContextTypes.DEFAULT_TYPE):
    with open('../text_commands_files/info_price.md','r') as f:
        price:str = f.read()
    await update.message.reply_html(price)

async def lunch_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [
            InlineKeyboardButton("Cap", callback_data='lunch_Cap'),
            InlineKeyboardButton("Cco", callback_data='lunch_Cco'),
            InlineKeyboardButton("Cdb", callback_data='lunch_Cdb'),
            InlineKeyboardButton("Csa", callback_data='lunch_Csa'),
            InlineKeyboardButton("Csl", callback_data='lunch_Csl'),
            InlineKeyboardButton("Ctan", callback_data='lunch_Ctan')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Qual ru deseja consultar o cardápio do almoço ? \U0001F914", reply_markup = reply_markup)

async def lunch_menus(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    choice = query.data
    
    if (choice == 'lunch_Cap'):
        try:
            menu:str = '../csv/cap_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'lunch_Csl'):
        try:
            menu:str = '../csv/csl_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format_2(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'lunch_Cco'):
        try:
            menu:str = '../csv/cco_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format_2(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
       
    elif choice == 'lunch_Cdb':
        try:
            menu:str = '../csv/cdb_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format_2(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')            

    elif choice == 'lunch_Csa':
        try:
            menu:str = '../csv/csa_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')

    elif choice == 'lunch_Ctan':
        try:
            menu:str = '../csv/ctan_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_lunch = lunch_filter(menu, date)
            await query.edit_message_text(response_format(response_lunch), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
    else:
        await query.message.reply_text('Selecione uma opção válida. \U0001F605 !', parse_mode = 'Markdown')

async def dinner_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    keyboard = [
        [
            InlineKeyboardButton("Cap", callback_data='dinner_Cap'),
            InlineKeyboardButton("Cco", callback_data='dinner_Cco'),
            InlineKeyboardButton("Cdb", callback_data='dinner_Cdb'),
            InlineKeyboardButton("Csa", callback_data='dinner_Csa'),
            InlineKeyboardButton("Csl", callback_data='dinner_Csl'),
            InlineKeyboardButton("Ctan", callback_data='dinner_Ctan')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Qual ru deseja consultar o cardápio do jantar ? \U0001F914", reply_markup = reply_markup)

async def dinner_menus(update:Update, context: ContextTypes.DEFAULT_TYPE):
    
    query = update.callback_query
    choice = query.data

    if (choice == 'dinner_Cap'):
        try:
            menu:str = '../csv/cap_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'dinner_Csl'):
        try:
            menu:str = '../csv/csl_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
        
    elif (choice == 'dinner_Cco'):
        try:
            menu:str = '../csv/cco_menu.csv'
            date:datetime.datetime = query.message.date.today()
            
            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
       
    elif choice == 'dinner_Cdb':
        try:
            menu:str = '../csv/cdb_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format_2(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')            

    elif choice == 'dinner_Csa':
        try:
            menu:str = '../csv/csa_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')

    elif choice == 'dinner_Ctan':
        try:
            menu:str = '../csv/ctan_menu.csv'
            date:datetime.datetime = query.message.date.today()

            response_dinner = dinner_filter(menu, date)
            await query.edit_message_text(response_format(response_dinner), parse_mode = 'Markdown')
        except:
            await query.message.reply_text('*Cardápio indisponível* \U0001F625 !', parse_mode = 'Markdown')
    else:
        await query.message.reply_text('Selecione uma opção válida. \U0001F605 !', parse_mode = 'Markdown')

#responses
def handle_responses(text: str, date) -> str:
    
    processed:str = text.lower()
    
    if ('almoço ctan' in processed) or ('almoco ctan' in processed):
        try:
            menu = '../csv/ctan_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'
    
    elif ('almoço csa' in processed) or ('almoco csa' in processed):
        try:
            menu = '../csv/csa_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço cdb' in processed) or ('almoco cdb' in processed):
        try:
            menu = '../csv/cdb_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format_2(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço cco' in processed) or ('almoco cco' in processed):
        try:
            menu = '../csv/cco_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format_2(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço csl' in processed) or ('almoco csl' in processed):
        try:
            menu = '../csv/csl_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format_2(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'

    elif ('almoço cap' in processed) or ('almoco cap' in processed):
        try:
            menu = '../csv/cap_menu.csv'
            response_lunch = lunch_filter(menu, date)
            
            return response_format(response_lunch)
        except:
            return '*Cardápio indisponível* \U0001F625 !'
    
    elif ('jantar cdb' in processed) or ('janta cdb' in processed):
        
        try:
            menu:str = '../csv/cdb_menu.csv'
            response_dinner = dinner_filter(menu, date)

            return response_format_2(response_dinner)
        except:
            return '*Cardápio indisponível* \U0001F625 !'
    
    elif ('jantar ctan' in processed) or ('janta ctan' in processed):
        
        try:
            menu = '../csv/ctan_menu.csv'
            response_dinner = dinner_filter(menu, date)

            return response_format(response_dinner)
        except:
            return '*Cardápio indisponível* \U0001F625 !'
        
    return 'Não entendi a sua mensagem. \U0001F605! /ajuda '

#When call this function, pass too the BOT_USERNAME
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    message_type = update.message.chat.type
    #print("message_type")
    text: str = update.message.text
    date = update.message.date.today()

    #Debug information
    #print(f'User({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':

        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME,'').strip()
            #print(new_text)
            response: str = handle_responses(new_text, date)
        else:
            return
    else:
        response: str = handle_responses(text,date)

    #print('Bot', response)
    await update.message.reply_text(response, parse_mode = 'Markdown')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass
    #print(f'Update{update} coused error {context.error}')