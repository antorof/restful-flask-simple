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
from flask import Flask, url_for, render_template, Response
import random
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid
    
""" ----------------------------------------------------------------------------------------------------------------
SSBW
"""

# @app.route('/')
# def api_root():
    # return 'Bienvenido'

# /hola -> 'Hola -cañon-'  (el string 'hola -cañón-' como txt, la ñ y la ó se deben ver bien en el navegador)
@app.route('/hola')
def api_hola():
    resp = 'Hola -cañón-'
    return Response(resp, mimetype='text/plain')

# /imagen  -> una imágen que tengamos preparada
@app.route('/imagen')
def api_imagen():
    resp = 'No implementado'
    return Response(resp, mimetype='text/plain')

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
@app.route('/circulos_varios/<numcirculos>')
def api_circulos(numcirculos=3):
    circulos = []
    colores = ['red','green','blue','purple','brown','yellow']
    for i in range(int(numcirculos)):
        circulos.append( [random.randint(50, 200),random.randint(50, 200),random.randint(20, 50)] )
    resp = '<svg height="400" width="400">'
    for i in range(int(numcirculos)):
        resp += '<circle cx="%s" cy="%s" r="%s" stroke="black" stroke-width="3" fill="%s" />' % (circulos[i][0],circulos[i][1],circulos[i][2],colores[random.randint(0, len(colores)-1)])
    resp += '</svg>'
    return Response(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
