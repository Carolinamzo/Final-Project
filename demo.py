#Importamos librerías
import pandas as pd
import numpy as np

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Cargamos los CSV's
df= pd.read_csv('IMDb movies.csv')
ratings = pd.read_csv('IMDb ratings.csv', index_col='imdb_title_id')

#Ajustamos y dropeamos los valores nulos
df.year = df.year.replace('TV Movie 2019', 2019).astype(int)

df['primary_genre'] = df.genre.apply(lambda x: x.split(',')[0])

df['primary_language'] = df.language.dropna().apply(lambda x: x.split(',')[0])

df['primary_country'] = df.country.dropna().apply(lambda x: x.split(',')[0])

#Aplicamos el relleno de las filas vacías
for i in ratings.columns[1:]:
    ratings[i] = ratings[i].fillna(value = ratings[i].median())

#Transponemos los Ratings para obtener la matriz
rat_trans=ratings.T
rat_trans.columns=df['original_title']

#Cambiamos los dtypes de las columnas
categ = [i for i in df.columns if df[i].dtype == 'O']
numeric = [i for i in df.columns if df[i].dtype != 'O']


#Sistema de recomendación de películas
def get_recommendations_for(title,n=10):
    if (len(title.split())==1):
        title=title.capitalize()
    else:
        pass
    
    top=rat_trans.corrwith(rat_trans[title]).sort_values(ascending=False)[1:n+1]
    print('='*125)
    print('='*125)
    print(f" Name: {df[df.original_title==title]['original_title'].values[0]}")
    print(f" Cast: {df[df.original_title==title]['actors'].values[0]}")
    print(f" Language: {df[df.original_title==title]['language'].values[0]}")
    print(f" Genre: {df[df.original_title==title]['genre'].values[0]}")
    print(f" Year: {df[df.original_title==title]['year'].values[0]}")
    print(f" Description: {df[df.original_title==title]['description'].values[0]}")
    print('='*125)
    print('*'*125)
    
    for t in top.index:
        
        print('='*125)
        print('|' + ' '*123+'|')
        
        print(f"| Movie Name: {df[df.original_title==t]['original_title'].values[0]}")
        print(f"| Director: {df[df.original_title==t]['director'].values[0]}")
        print(f"| Cast: {df[df.original_title==t]['actors'].values[0]}")
        print(f"| Language: {df[df.original_title==t]['language'].values[0]}")
        print(f"| Genre: {df[df.original_title==t]['genre'].values[0]}")
        print(f"| Year: {df[df.original_title==t]['year'].values[0]}")
        print(f"| Country: {df[df.original_title==t]['country'].values[0]}")
        print(f"| Description: {df[df.original_title==t]['description'].values[0]}")
        print(f"| Rating: {df[df.original_title==t]['avg_vote'].values[0]}")
        print(f"| Total Votes: {df[df.original_title==t]['votes'].values[0]}")
    
        print('|' + ' '*123+'|')
        print('='*125)
        print('-'*125)


#Dibujamos la consola
print('•••••••••••••••••••••••••••••••••••••••••••••••••••')
print('•                                                 •')
print('•                                                 •')
print("•       Bienvenido a PyMovie Recommendations      •")
print('•                                                 •')
print('•                                                 •')
print('•••••••••••••••••••••••••••••••••••••••••••••••••••')
print('')
print('')
print('')
print(input('*** PRESIONA ENTER PARA CONTINUAR ***'))
print('')
print('')
print(' ¿Cuál es tu usuario? ')
miNombre = input()

#Bienvenida
print('•••••••••••••••••••••••••••••••••••••••••••••••••••')
print('•                                                 •')
print('•                                                 •')
print("•            Bienvenido/a",miNombre,'             •')
print('•                                                 •')
print('•                                                 •')
print('•••••••••••••••••••••••••••••••••••••••••••••••••••')
print('')
print('')
print('')
print(input('*** PRESIONA ENTER PARA CONTINUAR ***'))
print('')
print('•••••••••••••••••••••••••••••••••••••••••••••••••••')
print('•                                                 •')
print('•       A continuación te presentaré un           •')
print("•            menú interactivo para                •")
print('•          recomendarte peliculas =D              •')
print('•                                                 •')
print('•••••••••••••••••••••••••••••••••••••••••••••••••••')
print('')
print('')

#recomendación de peliculas 

while True:
    print('')
    print(""" Menú PyMovies:
    1) Recomiendame una película
    2) Salir""")
    
    opcion = input()

    if opcion == '1':
    	try:
    		print('Introduce una pelicula que hayas visto: ')
    		pelicula = input()
    		get_recommendations_for(pelicula)

    		print('''¿Deseas volver a recomendarte una película?
    			     1) Recomiendame una película
    			     2) Salir''')
    		opcion = input()

    		continue

    	except KeyError:
    		print('¡Lo siento! La película que introdujiste no está en nuestra base de datos o el nombre es incorrecto.')

    elif opcion =='2':
    	print("¡Hasta luego! Ha sido un placer ayudarte")

    	break
    
    else:
        print("Comando desconocido, vuelve a intentarlo")
        print('')
