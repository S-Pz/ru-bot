from app.utils.format_data import output_formated
from app.services.ctan_service import find_by_data_and_horario

def format_data(horario:str, data:str)-> str:
    response = find_by_data_and_horario(horario=horario, data=data)
    response = output_formated(response)

    return response