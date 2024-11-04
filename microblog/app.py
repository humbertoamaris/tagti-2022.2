from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():

    return render_template("contato.html", tel="(87) 988889898", email="humberto.lima@aluno.ifsertao-pe.edu.br")
  
@app.route("/dados")
def dados(): 
    return render_template("dados.ht", tel="(87) 988889898")


if __name__ == '__main__':
    app.run()
