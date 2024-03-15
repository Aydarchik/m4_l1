from flask import Flask, render_template, request
import string
p_symbols = "#!\{}/+&@._§%?<>£;,:"
import random

app = Flask(__name__)

@app.route("/")
def index():
   return '<p>Привет пупс</p>''<a href="/facts_list">Посмотреть случайный факт!</a>''<p>Привет пупс</p>''<a href="/coin">Брось монетку!</a>'
@app.route("/facts_list")
def facts_list():
    facts_list = [
        'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
        'Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.',
        'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.'
    ]
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/coin")
def coins():
    coin = [
        'орёл',
        'решка',
    ]
    return f'<p>{random.choice(coin)}</p>'


    
    
app.run(debug=True)