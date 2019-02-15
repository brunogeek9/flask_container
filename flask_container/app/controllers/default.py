from app import app

@app.route("/")
def index():
    return "<h1> Bem vindo </h1>"

@app.route("/quantidade/<nome>/<qtd>")
def pizza(nome,qtd):
    return nome+" gosta de comer "+qtd

@app.route("/puppy_latin/<name>")
def puppy(name):
    new_name = ""
    if name[-1] != 'y':
        new_name = name + "y"
    else:
        new_name = name.replace("y","iful")

    return "o nome do doginho é {} e em latin o seu nome é {} tata".format(name,new_name)