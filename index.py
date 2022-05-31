#import libreria Flask
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#ruta principal en la que tendremos nuestra pagina de inicio de sesion
@app.route('/')
def helloworld():
    return render_template("index.html")

#Ruta de a pagina registro
@app.route('/registro.html/')
def registro():
    #Retornamos Template registro
    return render_template("registro.html")

#Ruta de la pagina tienda
@app.route('/tienda.html/')
def tienda():
    #Retornamos Template tienda
    return render_template("tienda.html")

#Ruta de la pagina Admin
@app.route('/Admin.html/')
def Admin():
    #Retornamos Template Admin
    return render_template("Admin.html")

if __name__ == "__main__":
    app.run(debug=True)