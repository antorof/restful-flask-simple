#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Crear un pequeño servidor web que devuelva a partir de los siguientes urls:

/hola   -> 'Hola -cañon-'  (el string 'hola -cañón-' como txt, la ñ y la ó se deben ver bien en el navegador)
/imagen  -> una imágen que tengamos preparada
/hola_pepe  -> 'Hola <b>Pepe</b>'  como html
/pagina  -> una página html que tengamos preparada, con un archivo css aparte
/circulos_varios  -> una arhivo svg con circulos generados  aleatoriamente en cada requermiento

Para cada respuesta, habrá que poner la cabecera 'Content-Type' con su tipo mime correspondiente

Usaremos un microframework como http://webpy.org o http://flask.pocoo.org
En http://blog.luisrei.com/articles/flaskrest.html hay una aplicación parecida
"""
from flask import Flask, url_for, render_template, Response, send_file
import random
app = Flask(__name__)

    
""" ----------------------------------------------------------------------------------------------------------------
SSBW
"""

@app.route('/')
def api_root():
    resp = 'Bienvenido'
    return Response(resp, mimetype='text/plain')

# /hola -> 'Hola -cañon-'  (el string 'hola -cañón-' como txt, la ñ y la ó se deben ver bien en el navegador)
@app.route('/hola')
def api_hola():
    resp = 'Hola -cañón-'
    return Response(resp, mimetype='text/plain')

# /imagen  -> una imágen que tengamos preparada
@app.route('/imagen')
def api_imagen():
    rutaImagen = 'static/imagen.jpg'
    return send_file(rutaImagen, mimetype='image/jpg')

# /hola_pepe -> 'Hola <b>Pepe</b>' como html
@app.route('/hola_pepe')
def api_hola_pepe():
    resp = 'Hola <b>Pepe</b>'
    return Response(resp, mimetype='text/html')

# /pagina -> una página html que tengamos preparada, con un archivo css aparte
@app.route('/pagina')
def api_pagina():
    html = render_template('mihtml.html')
    return Response(html, mimetype='text/html')

# /circulos_varios  -> una arhivo svg con circulos generados  aleatoriamente en cada requermiento
@app.route('/circulos_varios')
@app.route('/circulos_varios/<int:numcirculos>')
def api_circulos(numcirculos=3):
    circulos = []
    colores = ['red','green','blue','purple','brown','yellow','black','pink','white']
    for i in range(numcirculos):
        circulos.append( [random.randint(50, 200),random.randint(50, 200),random.randint(20, 50)] )
    resp = '<svg height="400" width="400">'
    for i in range(numcirculos):
        resp += '<circle cx="%s" cy="%s" r="%s" stroke="black" stroke-width="3" fill="%s" />' % (circulos[i][0],circulos[i][1],circulos[i][2],colores[random.randint(0, len(colores)-1)])
    
    return Response(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
