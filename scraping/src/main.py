import os
import pathlib

from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List, Optional

from dotenv import load_dotenv
from screpping import obtain_menus

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


urls:dict = {

    'csa':'https://ufsj.edu.br/proae/ru_csa.php',
    'ctan': 'https://ufsj.edu.br/proae/ru-ctan.php',
    'cdb': 'https://ufsj.edu.br/proae/ru_cdb.php',
    'csl': 'https://ufsj.edu.br/proae/r-csl.php',
    'cco': 'https://ufsj.edu.br/proae/r-cco.php',
    'cap': 'https://ufsj.edu.br/proae/r-cap.php'
}

format_content:list = [
  {
    "data": "DD/MM/YYYY",
    "dia_semana": "Segunda-feira",
    "almoco": {"prato_principal": "...", 
               "vegetariano":"...", 
               "guarnicao": "...",
               "salada1": "...",
               "salada2": "...",
               "feijao": "...", 
               "suco": "...", 
               "sobremesa": "..."
               }

  },
  {

    "data": "DD/MM/YYYY",
    "diaDaSemana": "Segunda-feira",
    "jantar": {"pratoPrincipal": "...",
               "vegetariano":"...",
               "guarnicao": "...",
               "salada1": "...",
               "salada2": "...",
               "feijao": "...",
               "suco": "...",
               "sobremesa": "..."
               }

  },
]

def main():
    
    for i in urls:
        obtain_menus(urls[i], str(i))

    file_path_ctan = pathlib.Path('../Menus/ctan.pdf')

    prompt = f"Extrai do pdf o cadápio seguindo estruta json fornecida e não coloque o valor dos campos em caixa alta: {format_content}" 

    client = genai.Client(api_key= GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
            data=file_path_ctan.read_bytes(),
            mime_type='application/pdf',
        ),
        prompt]
    )
    
if __name__ == '__main__':
   main()