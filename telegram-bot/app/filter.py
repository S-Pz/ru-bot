import pandas as pd
import datetime

def format_date(date:datetime.datetime) -> str: # format date
    
    formated = date.strftime('%d/%m')

    return formated

def lunch_filter(filepath:str, date:datetime.datetime) -> list: # make a filter for lunch
    
    current_date = format_date(date)
    
    lunch_df = pd.read_csv(filepath, encoding='utf-8')

    mask = (lunch_df["DATA"] == current_date) & (lunch_df["HORARIO"].str.lower() == "Almoço".lower()) 
   
    df_list = lunch_df[mask].values.tolist()

    return df_list

def dinner_filter(filepath:str, date:datetime.datetime) -> list: # make a filter for dinner

    current_date = format_date(date)
    
    dinner_df = pd.read_csv(filepath, encoding = 'utf-8')

    mask = (dinner_df["DATA"] == current_date) & (dinner_df["HORARIO"].str.lower() == "Jantar".lower())

    df_list = dinner_df[mask].values.tolist()

    return df_list

def response_format(text:list) -> str: # format response
    
    print(text)

    header = "📅* "+ str(text[0][0]) + "*" + " *"+ str(text[0][1] +":*\t\t🍽️\n\n")
    main_lawn = "🍴 *Prato Principal:* " + str(text[0][2])+ "\n\n"
    eggs = "🥚 *OVOS:* " + str(text[0][3]) + "\n"
    veg = "🥬 *VEGETARIANO:* " + str(text[0][4]) + "\n"
    garn = "🍝 *GUARNIÇÃO:* " + str(text[0][5]) + "\n"
    rice = "🍚 *ARROZ:* " + str(text[0][6]) + "\n"
    bean = "🫘 *FEIJÃO:* " + str(text[0][7]) + "\n"
    sal= "🥗 *SALADAS:* " + str(text[0][8]) + " / " + str(text[0][9]) + "\n"
    juice = "🧃 *SUCO:* " + str(text[0][10]) + "\n"
    dess = "🍬 🍎 *SOBREMESA:* " + str(text[0][11]) + "\n"

    response_text = header + main_lawn + eggs + veg + garn + rice + bean + sal+ juice + dess
    
    return response_text

def response_format_2(text:list) -> str: # format response #cdb, csl, cco
    print(text)

    header = "📅* "+ str(text[0][0]) + "*" + " *"+ str(text[0][1] +":*\t\t🍽️\n\n")
    main_lawn = "🍴 *Prato Principal:* " + str(text[0][2])+ "\n\n"
    eggs = "🥚 *OVOS:* " + str(text[0][3]) + "\n"
    veg = "🥬 *VEGETARIANO:* " + str(text[0][4]) + "\n"
    garn = "🍝 *GUARNIÇÃO:* " + str(text[0][5]) + "\n"
    sal= "🥗 *SALADAS:* " + str(text[0][6]) + " / " + str(text[0][7]) + "\n"
    rice = "🍚 *ARROZ:* " + str(text[0][8]) + "\n"
    bean = "🫘 *FEIJÃO:* " + str(text[0][9]) + "\n"
    dess = "🍬 🍎 *SOBREMESA:* " + str(text[0][10]) + "\n"
    juice = "🧃 *SUCO:* " + str(text[0][11]) + "\n"

    response_text = header + main_lawn + eggs + veg + garn + rice + bean + sal+ juice + dess
    
    return response_text