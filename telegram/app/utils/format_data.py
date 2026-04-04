def output_formated(data:dict)-> str:

    header = "📅 *"+ data.get("data") + "*" + " | " + "*"+ data.get("diaDaSemana") +"*\n\n"
    main_course = "🍴 *Prato Principal:* " + data.get("pratoPricipal")+ "\n\n"
    vege = "🥬 *VEGETARIANO:* " + data.get("vegetariano") + "\n"
    garni = "🍝 *GUARNIÇÃO:* " + data.get("guarnicao") + "\n"
    bean = "🫘 *FEIJÃO:* " + data.get("feijao") + "\n"
    #sal= "🥗 *SALADAS:* " + data.get("salada1") + " / " + data.get("salada2") + "\n"
    juice = "🧃 *SUCO:* " + data.get("suco") + "\n"
    dess = "🍬/🍎 *SOBREMESA:* " + data.get("sobremesa") + "\n"

    response = header + main_course + vege + garni + bean + juice + dess
    
    return response