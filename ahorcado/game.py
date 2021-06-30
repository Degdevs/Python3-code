import random

#Todas en mayusculas xq es una constante
IMÁGENES_AHORCADO = ['''

 +---+
 | |
 |
 |
 |
 |
 =========''', '''
 +---+
 | |
 O |
 |
 |
 |
 =========''', '''

 +---+
 | |
 O |
 | |
 |
 |
 =========''', '''

 +---+
 | |
 O |
 /| |
 |
 |
 =========''', '''

 +---+
 | |
 O |
 /|\ |
 |
 |
 =========''', '''

 +---+
 | |
 O |
 /|\ |
 / |
 |
 =========''', '''

 +---+
 | |
 O |
 /|\ |
 / \ |
 |
 =========''']

# el .split() ) devuelve una lista en la que cada palabra en la cadena es un elemento aparte. La separación ocurre en cualquier lugar donde haya un espacio en la cadena.
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAlAzar (listaDePalabras):
    # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    
    print('Letras Incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')

    espaciosVacios = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): #completar los espacios vacios co las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]
        
        for letra in espaciosVacios: #mostrar la palabra secreta con espacios entre cada letra
            print(letra, end=' ')
        print()

def obtenerIntento(letrasProbadas): #devuelve la letra ingresada x el jugador y verifica que se haya ingreasdo una letra y no optra cosa
    while True:
        print('Adivina una letra')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor introducir una letra')
        elif intento in letrasProbadas:
            print('Ya probaste con esa letra, introduce otra')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor introducir una LETRA')
        else:
            return intento

def jugarDeNuevo():   # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('Queres jugar de nuevo?')
    return input().lower().startswith('s')

print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
    #permite al jugador ingresar letras
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento
        #verifica si el jugador gano  
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('Ganaste!! adivinaste la palabra ' + palabraSecreta)
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
        #verifica si el jugador agoto sus intentos
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(IMÁGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('Te quedaste sin intentos!!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True
        #preguntar al jugador si quiere volver a jugar
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break   
