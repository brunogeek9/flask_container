from app import app

@app.route("/")
def index():
    return "opa"

@app.route("/jamelli")
def jamelli():
    return "gosta de feijão"

@app.route("/quantidade/<nome>/<qtd>")
def pizza(nome,qtd):
    return nome+" gosta de comer "+qtd