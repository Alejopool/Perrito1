from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#--------------------------ESPACIO  PARA LAS FUNCIONES DEL PROYECTO--------------------------------
def contar_cadenas(cadena1, cadena2):
    resultados = {}

    if cadena1.isdigit() or cadena2.isdigit():
        return "No puedo contar, alguna de las 2 cadenas tiene números", resultados

    cant_digitos1 = len(cadena1)
    cant_digitos2 = len(cadena2)

    if cant_digitos1 == cant_digitos2:
        resultados['Cadena1'] = contar_vocales(cadena1)
        resultados['Cadena2'] = contar_vocales(cadena2)
    else:
        return "Las cadenas no tienen la misma cantidad de caracteres", resultados

    return None, resultados

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = 'aeiou'
    contador = {vocal: 0 for vocal in vocales}

    for char in cadena:
        if char in vocales:
            contador[char] += 1

    return {vocal: contador[vocal] for vocal in vocales if contador[vocal] > 0}
#--------------------------------------------------------------------------------------------------

@app.route('/')  # Inicializa el servidor en la raíz del proyecto
def llevar_inicio(): 
    return render_template('index.html')

@app.route('/Conteo_vocales', methods=['GET', 'POST'])  # Enviar a ruta de conteo de vocales
def ingreso_conteo_vocales(): 
    resultados = {}
    mensaje_error = None

    if request.method == 'POST':
        cadena1 = request.form.get('Cadena1')
        cadena2 = request.form.get('Cadena2')

        mensaje_error, resultados = contar_cadenas(cadena1, cadena2)

    return render_template('Conteo_vocales.html', resultados=resultados, mensaje_error=mensaje_error)

@app.route('/Sub_cadena')  # Enviar a ruta de subcadenas
def ingreso_Sub_cadena(): 
    return render_template('Sub_cadena.html')

@app.route('/Palindromas')  # Enviar a ruta de palíndromas
def ingreso_Palindromas(): 
    return render_template('Palindromas.html')

@app.route('/Titulo_mayuscula')  # Enviar a ruta de título mayúscula
def ingreso_Titulo_mayuscula(): 
    return render_template('Titulo_mayuscula.html')

@app.route('/seleccionar', methods=['POST'])  # Enviar a ruta de selección
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
