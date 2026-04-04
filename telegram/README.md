# :robot: Uni-Meal-Bot

## :bookmark_tabs: Sobre o Bot
O projeto visa criar um **bot** que funcione como uma ferramenta dupla: oferecendo **consulta rápida ao cardápio** e um **meio de acessar um formulário para reportar casos de intoxicação alimentar.** 
A necessidade dessa solução surgiu entre os usuários dos restaurantes universitários (RU) da [UFSJ](https://www.ufsj.edu.br/), confrontados com desafios para verificar o cardápio diário e para preencher (ou mesmo descobrir a existência de) um formulário específico após experiências adversas com as refeições oferecidas. 
Atualmente, para acessar o cardápio, os usuários precisam navegar pelo site da universidade, localizar o RU de seu campus, baixar o arquivo correspondente e então procurar a informação desejada, um processo que se mostra ineficiente e demanda tempo.

## :clipboard: Bibliotecas / _Requirements_ 
As bibliotecas necessárias estão no arquivo `requirements.txt` para instalar execute:

```sh
pip install -r requirements.txt
```

## :paperclip: Env e Venv
Para trabalhar crie uma ambiente virtual, para as bibliotecas não entrarem em conflito de versões. Para criar um ambiente virtual utilizando o **Venv** dentro do diretório raiz do projeto execute:

```sh
python -m venv .venv
```
Para **inciar** o ambiente:
```sh
source .venv/bin/activate
```
Para **desativar**:
```sh
deactivate
```