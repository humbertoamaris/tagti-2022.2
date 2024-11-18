from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():

    return render_template("contato.html", tel="(87) 988889898", email="humberto.lima@aluno.ifsertao-pe.edu.br")
  
@app.route("/dados")
def dados(): 
    return render_template("dados.html", tel="(87) 988889894", email="humberto.lima@aluno.ifsertao-pe.edu.br")


@app.route('/recebedados', methods=['POST'])
def recebedados():


