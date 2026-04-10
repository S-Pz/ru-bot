import os
import requests as req
from dotenv import load_dotenv

load_dotenv()

API_BASE_PATH = os.getenv('API_BASE_PATH')

def save_ctan_menu (data):
   
    response = req.post(f"{API_BASE_PATH}/ctan", data = data)

    if response.status_code == "201":
        print("Cardápio Ctan salvo com sucesso")
