from flask import Flask, render_template, redirect, request
from filmes import pegarfilme


app = Flask(__name__) 


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['nome_filme']
    return redirect(f'/{name}')


@app.route("/<name>")
def filme(name=None):
    if name:
        filmedic = pegarfilme(name)
        return render_template('index.html', **filmedic)
    else:
        return "Olá!"
    
if __name__ == "__main__":
    app.run(host = "localhost", port = 5002, debug = True)