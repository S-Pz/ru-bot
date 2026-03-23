from screpping import obtain_menus

urls:dict = {

    'csa':'https://ufsj.edu.br/proae/ru_csa.php',
    'ctan': 'https://ufsj.edu.br/proae/ru-ctan.php',
    'cdb': 'https://ufsj.edu.br/proae/ru_cdb.php',
    'csl': 'https://ufsj.edu.br/proae/r-csl.php',
    'cco': 'https://ufsj.edu.br/proae/r-cco.php',
    'cap': 'https://ufsj.edu.br/proae/r-cap.php'
}

if __name__ == '__main__':

    for i in urls:
        obtain_menus(urls[i], str(i))