# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:15:13 2018

@author: LAC40641
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:13:18 2018

@author: LAC40641
"""

from elasticsearch import Elasticsearch
import json
import time
import csv

ES_HOST = 'https://search-adm-35ohesxnchgmztcblylrwe3dvu.us-east-1.es.amazonaws.com'
es = Elasticsearch(ES_HOST)

number = 0

directorio = 'C:\\Users\\LAC40641\\Desktop\\'

file = open(directorio+'carga_datos.csv', "rU")
reader = csv.reader(file, delimiter=',')

for row in reader:
    print(row[0])
    palabra = row[0]
    pagina = row[1]
    palabra_busqueda = row[2]
    cantidad = row[3]
    fechaini = row[4]
    fechafin = row[5]
    global number
    number += 1

    go = es.index(
        index="busqueda_palabra_clave",
        doc_type="busqueda",
        id=str(number),
        body={
            "palabra": palabra,
            "pagina": pagina,
            "palabra_busqueda": palabra_busqueda,
            "cantidad": cantidad,
            "fechaini": fechaini,
            "fechafin": fechafin,
        }
    )

    print (json.dumps(go))
    time.sleep(0.01)


