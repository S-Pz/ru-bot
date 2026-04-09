import datetime

from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.lunch_menu_handlers import lunch_daily_ctan_callback

async def automatic_message_callback (update:Update, context:ContextTypes.DEFAULT_TYPE):
    
    callback_query = update.callback_query
    await callback_query.answer()

    callback_data = callback_query.data
    chat_id = update.effective_chat.id

    if(callback_data == "auto_ctan"):
        
        job_name = f"auto_ctan_{chat_id}"
        current_jobs = context.job_queue.get_jobs_by_name(job_name)

        if current_jobs:
            for job in current_jobs:
                job.schedule_removal()
            
            await context.bot.send_message(
                chat_id = chat_id, 
                text = "Notificação diária do CTAN desativada!"
            )
        else:
            horario_envio = datetime.time(hour=10, minute=0)

            context.job_queue.run_daily(
                lunch_daily_ctan_callback,
                time = horario_envio,
                days = (0,1,2,3,4,5),
                chat_id = chat_id,
                name = job_name
            )

            await context.bot.send_message(
                chat_id = chat_id, 
                text="Notificação ativada!"
            )