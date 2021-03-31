![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# PyMovie: Analysis & Recommender Sys
***
PyMovie es un sistema de recomendaciones a partir de un filtrado colaborativo, donde empareja a personas con intereses similares y proporciona recomendaciones basadas en esta coincidencia. 
Además, proporciona un análisis de películas con base en su género, país de producción, idiomas, compañías, así como un profundo análisis de películas hechas en México. 
Podemos consultar la información más relevante de las películas, tales son el nombre del director, su cast, visualizar los gráficos y generar indicadores, consultar información a detalle de cada película.

## Estructura del demo
***
La estructura del demo se compone de las siguientes opciones:

1. Menú interactivo con el usuario

Podemos seleccionar las opciones que nos da el menú e introducir el nombre de una película que hayas visto. 

2. Sistema de recomendaciones

A partir del título de la película seleccionada, nos despliega 10 películas categóricas con base en el sistema de recomendaciones por filtración colaborativo, así como las coincidencias más próximas al título introducido. 

3. Información a detalle

Cada película recomendada, saldrá información a detalle sobre el año y país de producción, el director, su cast, la sinópsis, y la/s compañía/s que fueron producidas.

## Fuentes de información
***
Librería IMDb
https://imdbpy.github.io/

Base de datos IMBd - actualizada al 2020 -
https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset

Sistema de recomendaciones
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html

## Siguientes pasos
***
Esta versión PyMovie es la primera, el proyecto es completamente escalable, por lo que invito a cualquier persona interesada a contactarme para cualquier tipo de aportaciones es completamente bienvenida, desde la propuesa para mejorar las funcionalidades. 

Igualmente, para futuras versiones, se escala a un dashboard y sea más interactivo con el usuario. 