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

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user,passw = 'laiun.ce@gmail.com','Lw8dyr15'

ES_HOST = 'https://search-adm-35ohesxnchgmztcblylrwe3dvu.us-east-1.es.amazonaws.com'
es = Elasticsearch(ES_HOST,  verify_certs=False)


number = 0

#directorio = 'C:\\Users\\LAC40641\\Desktop\\'
directorio = '/Users/laiunce/Documents/ADM/bajada_busqueda/bajadas/danielpelegrina/'

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
    number += 1

    print(fechaini[0:4]+'-'+fechaini[4:6]+'-'+fechaini[6:8])


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
            "datetime": fechaini[0:4]+'-'+fechaini[4:6]+'-'+fechaini[6:8]

        }
    )

    print (json.dumps(go))
    time.sleep(0.01)


