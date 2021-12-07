from flask import Flask
from flask import render_template, request, session

class Sala:
    def __init__(self):
        self.nome = ''
        self.senha = ''
        self.jogadores_nome = []
        self.jogadores_cor = []     
        self.cartas = []
        self.descarte_carros = []
        self.estado = 'escolhendo_objetivos'
        self.pontos = {}

sala = Sala()

app = Flask(__name__)
app.secret_key = b'123'

@app.route('/')
def index():
    context = {
    'sala': sala
    }
    
    return render_template('index.html', **context)

@app.route('/inicio', methods = ['GET', 'POST'])
def inicio():
    sala.nome = request.form['room_name']
    sala.senha = request.form['room_pswd']
    context = {
    'sala': sala
    }
    return render_template('inicio.html', **context)

@app.route('/jogo', methods = ['GET', 'POST'])
def jogo():

    nome_jogador = request.form.get('playername')
    session['name'] = nome_jogador
    sala.jogadores_nome.append(nome_jogador)
    cor_jogador = request.form.get('cor')
    sala.jogadores_cor.append(cor_jogador)
    context = {
    'sala': sala

    }
    return render_template('jogo.html', **context)