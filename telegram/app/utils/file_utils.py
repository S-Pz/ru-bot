import os
from functools import lru_cache

@lru_cache(maxsize=10)
def file_reader(directory:str, file_name:str)->str:

    file_path = os.path.join(os.path.abspath(directory), file_name)
    with open(file_path, encoding='utf-8', mode='r') as f:
        response = f.read()
    
    return response