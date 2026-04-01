from functools import lru_cache

@lru_cache(maxsize=10)
def file_reader(file_path:str)->str:
    response:str = ""

    with open(file_path, encoding='utf-8',mode='r') as f:
        response = f.read()
    
    return response