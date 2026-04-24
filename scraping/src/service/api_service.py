import os
import requests as req
from dotenv import load_dotenv

load_dotenv()

API_BASE_PATH = os.getenv('API_BASE_PATH')

def save_ctan_menu (data):
   
    try:
        response = req.post(f"{API_BASE_PATH}/ctan", json = data, timeout = 5)
        response.raise_for_status() 
        print(response.json()) 

    except req.exceptions.HTTPError as err:
        print(f"Erro de HTTP: {err}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

