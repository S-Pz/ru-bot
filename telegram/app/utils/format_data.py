import datetime

def output_formated(data:dict)-> str:
    
    date = datetime.datetime.strptime(data.get("data"), "%Y-%m-%d")
    
    header = "📅 *" + date.strftime("%d-%m-%Y") + "*" + " | " + "*" + data.get("diaDaSemana") + "*\n\n"
    main_course = "🍴 *PRATO PRINCIPAL:* " + data.get("pratoPricipal")+ "\n\n"
    vege = "🥬 *VEGETARIANO:* " + data.get("vegetariano") + "\n"
    garni = "🍝 *GUARNIÇÃO:* " + data.get("guarnicao") + "\n"
    bean = "🫘 *FEIJÃO:* " + data.get("feijao") + "\n"
    sal = "🥗 *SALADAS:* " + data.get("salada1") + " / " + data.get("salada2") + "\n"
    juice = "🧃 *SUCO:* " + data.get("suco") + "\n"
    dess = "🍬/🍎 *SOBREMESA:* " + data.get("sobremesa") + "\n"

    response = header + main_course + vege + garni + sal + bean + juice + dess
    
    return response