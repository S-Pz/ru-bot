import os
import pathlib
import json

from google import genai
from google.genai import types

from dotenv import load_dotenv

from utils.screpping import obtain_menus
from utils.formats import urls, format_json_prompt
from service.api_service import save_ctan_menu

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def use_ia(file_path:str, client, prompt:str):
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
            data=file_path.read_bytes(),
            mime_type='application/pdf',
        ),
        prompt]
    )

    return response.json()
        
def main():

    client = genai.Client(api_key= GEMINI_API_KEY)
    prompt = f"Extrai do pdf o cadápio seguindo estruta json fornecida e não coloque o valor dos campos em caixa alta escreva-os normalmente respeitando a letras maiúsculas e acentos, retorne apenas JSON válido, sem markdown (```), sem texto extra: {format_json_prompt}" 

    for i in urls:
        obtain_menus(urls[i], str(i))
        
        if str(i) == "ctan":
            file_path = pathlib.Path(f'../Menus/{str(i)}.pdf')
            response = use_ia(file_path = file_path, client = client, prompt = prompt)
            response = json.loads(response)
            save_ctan_menu(response)

    
if __name__ == '__main__':
   main()