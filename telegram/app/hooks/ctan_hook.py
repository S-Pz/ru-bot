from app.utils.format_data import output_formated
from app.services.ctan_service import find_by_date_and_horario

def date_and_horario_ctan(horario:str, data:str)-> str:
    response = find_by_date_and_horario(horario=horario, data=data)
    response = output_formated(response)

    return response