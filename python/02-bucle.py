with open('./python/fichero.csv', encoding='utf8') as fp:  
    linea = fp.readline();
    while linea:
        print(linea)
        linea = fp.readline();
        