from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#--------------------------ESPACIO  PARA LAS FUNCIONES DEL PROYECTO--------------------------------
#FUNCION CONTAR VOCALES ------------------
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
#---------------------------------------------
#FUNCION SUB CADENA --------------------------
class CadenaVerificadora:
    def verificar_subcadena(self, cadena1, cadena2):
        
        if len(cadena1) >= len(cadena2):
            largo = cadena1
            corto = cadena2
        else:
            largo = cadena2
            corto = cadena1
        
        if corto in largo:
            return f"{corto} ES SUBCADENA DE {largo}"
        else:
            return f"{corto} NO ES SUBCADENA DE {largo}"
#---------------------------------------------
#FUNCION BUSCAR PALINDROMAS ------------------
def FuncionPalindroma(Parrafo):
    CantidadESpacios = Parrafo.count(' ')
    Palabra = Parrafo.split()
    
    Palindroma = []
    Cobtador = 0
    while Cobtador < len(Palabra):
        if Palabra[Cobtador].lower() == Palabra[Cobtador][::-1].lower():
            Palindroma.append(Palabra[Cobtador])
        Cobtador += 1
        
    CantPalabraspalindromas = len(Palindroma)

    resultado = f"Numero de espacios en el parrafo: {CantidadESpacios}<br>"
    resultado += f"Hay {CantPalabraspalindromas} palabras palindromas en el texto digitado.<br>"
    
    if Palindroma:
        resultado += "Palabras palindromas encontradas:<br>"
        for palabra in Palindroma:
            resultado += f"{palabra}<br>"
    else:
        resultado += "No se encontraron palabras palindromas.<br>"

    return resultado
#---------------------------------------------
#FUNCION Titulos en Mayuscula ----------------
def titulo(cadena):
    if cadena.isdigit():
        return "lo que acaba de digitar son numeros"
        #quit()
    else:
        Palabras = cadena.split()
        resultado = ""
        i = 0

        while i < len(Palabras):
            PalabrasConPrimeraLetraMayuscula = Palabras[i].capitalize()

            if resultado:  
                resultado += " "
            
            resultado += PalabrasConPrimeraLetraMayuscula
            i += 1
        
        return resultado
#---------------------------------------------
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

@app.route('/Sub_cadena', methods=['GET', 'POST'])  # Enviar a ruta de subcadenas
def ingreso_Sub_cadena(): 
    verificador = CadenaVerificadora()
    Resultado = None
    if request.method == 'POST':
        Texto1 = request.form.get('Texto1')
        Texto2 = request.form.get('Texto2')
        Resultado = verificador.verificar_subcadena(Texto1,Texto2)

    return render_template('Sub_cadena.html',Resultado = Resultado)

@app.route('/Palindromas', methods=['GET', 'POST'])  # Enviar a ruta de palíndromas
def ingreso_Palindromas(): 
    Resultado = None

    if request.method == 'POST':
        palindromas = request.form.get('palindromas')
        Resultado = FuncionPalindroma(palindromas)

    return render_template('Palindromas.html', Resultado = Resultado)

@app.route('/Titulo_mayuscula', methods=['GET', 'POST'])  # Enviar a ruta de título mayúscula
def ingreso_Titulo_mayuscula(): 
    Resultado = None
    if request.method == 'POST':
        Titulo = request.form.get('Titulo')
        Resultado = titulo(Titulo)

    return render_template('Titulo_mayuscula.html', Resultado = Resultado)

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
