import os
import requests as req
from dotenv import load_dotenv

load_dotenv()

API_BASE_PATH = os.getenv('API_BASE_PATH')

def find_by_date_and_horario (horario:str, data:str):
   
    response = req.get(f"{API_BASE_PATH}/ctan", params={"horario":horario, "data":data})

    if (response.status_code == 200):
        return response.json()
    else:
        raise Exception(f"Non-success status code: {response.status_code}")
