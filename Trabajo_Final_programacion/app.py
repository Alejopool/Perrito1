from flask import Flask, render_template, request, redirect,url_for # importa las librerias especificas de flask

app = Flask(__name__) #este codigo me cambia el nombre por defecto

@app.route('/') # Inialice el servidor en la raiz del proyecto
def llevar_inicio(): 
    return render_template('index.html')

@app.route('/Conteo_vocales') # Eviar a ruta conteo de vocales
def ingreso_conteo_vocales(): 
    return render_template('Conteo_vocales.html')

@app.route('/Sub_cadena') # Eviar a ruta de subcadenas
def ingreso_Sub_cadena(): 
    return render_template('Sub_cadena.html')

@app.route('/Palindromas') # Eviar a ruta de spalindroma
def ingreso_Palindromas(): 
    return render_template('Palindromas.html')

@app.route('/Titulo_mayuscula') # Eviar a ruta de titulo mayuscula
def ingreso_Titulo_mayuscula(): 
    return render_template('Titulo_mayuscula.html')

@app.route('/seleccionar', methods = ['POST']) # Eviar a ruta de titulo mayuscula
def seleccionar(): 
    opcion = request.form.get('opcion')

    if opcion == 'sustentacion':
        return render_template('sustentacion.html') 
    elif opcion == 'manual_usuario':
        return render_template('manual_usuario.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)