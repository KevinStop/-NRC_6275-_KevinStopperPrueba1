#import libreria Flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#ruta principal en la que tendremos nuestra pagina de inicio de sesion
@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/registro.html/')
def registro():
    return render_template("registro.html")

@app.route('/tienda.html/')
def tienda():
    return render_template("tienda.html")

@app.route('/Admin.html/')
def Admin():
    return render_template("Admin.html")

if __name__ == "__main__":
    app.run(debug=True)