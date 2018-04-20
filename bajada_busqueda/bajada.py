#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:32:49 2018

@author: laiunce
"""


import requests
import re
import pandas as pd
import os

server_dir = '52.14.67.113'
server_dir = '0.0.0.0'

def limpia_texto(text):
    text=text.lower()
    text = text.replace("ñ", "n")
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u") 
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace(";", " ")        
    text = text.replace("[", " ")
    text = text.replace("]", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")        
    text = text.replace("{", " ")
    text = text.replace("}", " ")
    text = text.replace("?", " ")        
    text = text.replace("¿", " ")        
    text = text.replace("!", " ")        
    text = text.replace("¡", " ")    
    text = text.replace(":", " ")  
    return(re.sub('[^a-zA-Z\s]', '', text))


#pagina='https://www.revistavirtualpro.com/noticias/energia'    

def obtiene_texto_palabras_metricas(palabra_busqueda,pagina,fechaini,fechafin):

    path = "http://"+server_dir+":5000/api/v1/resources/get?webpage={}".format(pagina)
    r = requests.get(path) 
    te = (r.json().replace('\n',' '))      
    limp = limpia_texto(te)
    merge=''
    for rx in regex.split('|'):
        contexto = re.findall(r"(?s).{0,500}%s.{0,500}"%rx, limp)
        for t in contexto:
            merge=merge + ' '+t
            
    palabras_pagina = re.findall(r"[a-zA-Z]{4,20}", merge)
    
    df=pd.DataFrame(palabras_pagina)
    df.columns = ['palabra']
    df['pagina'] =pagina
    df['palabra_busqueda'] =palabra_busqueda
    df['cantidad'] = 1
    df['fechaini'] = fechaini
    df['fechafin'] = fechafin 
    
    return df


def crea_metricas_palabras(df1):
    #cantidad de veces aparecida
    palabras_count = pd.DataFrame(df1.groupby(['palabra'])['cantidad'].agg('sum'))
    #cantidad de veces aparecida en paginas distintas
    palabras_paginas_dif = pd.DataFrame(df1.groupby('palabra').pagina.nunique())
    #Se conviernte dataframe a json
    
    union = pd.merge(palabras_count, palabras_paginas_dif, left_index=True, right_index=True)
    union.columns = ['aparece_qty','paginas_diferentes_qty']
    union['fechaini'] = fechaini
    union['fechafin'] = fechafin
    union['palabra'] = union.index
    data_out.index
    
    return union



def devuelve_palabras_cantidades(busqueda,fechaini,fechafin,regex):
    print('obtiene paginas')
    #obtiene busquedas
    path = "http://"+server_dir+":5000/api/v1/resources/get_google_noticias?busqueda={}&fechaini={}&fechafin={}".format(busqueda,fechaini,fechafin)
    r = requests.get(path) 
    json = r.json()
    
    #por cada pagina obiene el texto
    
    print('cantidad de paginas: '+str(len(json)))
    
    df1 = pd.DataFrame()

    
    contador = 0
    for pagina in json:
        contador +=1
        print('va por pagina: '+str(contador)+' '+pagina)
        try:
            df = obtiene_texto_palabras_metricas(busqueda,pagina,fechaini,fechafin)
            df1= pd.concat([df1, df], ignore_index=True) 
        except:
            pass
    
    
    #crea dataframe con
    #palabra, cantidad de paginas, cantidad palabras
    
    #transformar a json
    #out = union.to_json(orient='records')[1:-1].replace('},{', '} {')
    
    return df1



#busqueda = 'pampa+energia+argentina'
#fechaini = '20170401'
#fechafin = '20170401'
#regex= 'energia pampa|petrolera pampa|pampa energia'

#directorio_salida='/Users/laiunce/Desktop/bajada_paginas/'

directorio_salida='/Users/laiunce/Documents/ADM/bajada_busqueda/'

#data_out = devuelve_palabras_cantidades(busqueda,fechaini,fechafin,regex)   

data_out_merged = pd.DataFrame()


busqueda = 'daniel+pelegrina'
#regex= 'macri.*puta.*pario'
regex= 'daniel.{0,10}pelegrina'


comando2= 'mkdir bajada/'+busqueda
#os.system(comando2)  
        
#fechas = ['20180411','20180412','20180413','20180414','20180415','20180416','20180417']
fechas = ['20180411','20180412','20180413','20180414','20180415','20180416','20180417']
for i in fechas:
    print(i)
    try:
        fechaini = i
        fechafin = i
        data_out = devuelve_palabras_cantidades(busqueda,fechaini,fechafin,regex)   
        #data_out_merged= pd.concat([data_out_merged, data_out], ignore_index=True)
        data_out.to_csv(directorio_salida+'bajadas/danielpelegrina/'+i+'.csv',index=False)
    except:
        pass




#daniel+pelegrina









    
    
