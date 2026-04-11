urls:dict = {

    'csa':'https://ufsj.edu.br/proae/ru_csa.php',
    'ctan': 'https://ufsj.edu.br/proae/ru-ctan.php',
    'cdb': 'https://ufsj.edu.br/proae/ru_cdb.php',
    'csl': 'https://ufsj.edu.br/proae/r-csl.php',
    'cco': 'https://ufsj.edu.br/proae/r-cco.php',
    'cap': 'https://ufsj.edu.br/proae/r-cap.php'
}

format_json_prompt:list = [
  {
    "data": "DD/MM/YYYY",
    "diaDaSemana": "Segunda-feira",
    "almoco": {"pratoPrincipal": "...", 
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