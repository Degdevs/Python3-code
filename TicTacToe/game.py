import random
#Definiendo funciones

def dibujarTablero(tablero):
    # tablero es una lista de 10 cadenas representadas en la pizarra

    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('-----------')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('-----------')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])


def ingresaLetraJugador(): #permite al jugador elegir que letra usar

    letra = ''
    
    while not (letra == 'X' or letra == 'O'):
        print('Deseas ser X o O?')
        letra = input().upper()
    
    if letra == 'X':    #el primer elemento de la lista es el jugador, el segundo la computadora
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza(): #elige aleatoreamente el priemor en jugar
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def jugarDeNuevo():
    print('Deseas volver a jugar? (si/no)')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):      # Dado un tablero y la letra de un jugador, devuelve True (verdadero) si el mismo ha ganado.
    #reemplazo tablero por ta y letra por le para no escribir tanto
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or # horizontal superior
    (ta[4] == le and ta[5] == le and ta[6] == le) or # horizontal medio
    (ta[1] == le and ta[2] == le and ta[3] == le) or # horizontal inferior

    (ta[7] == le and ta[4] == le and ta[1] == le) or # vertical izquierda
    (ta[8] == le and ta[5] == le and ta[2] == le) or # vertical medio
    (ta[9] == le and ta[6] == le and ta[3] == le) or # vertical derecha

    (ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
    (ta[9] == le and ta[5] == le and ta[1] == le)) # diagonal

def obtenerDuplicadoTablero(tablero):
    dupTablero = []

    for i in tablero:
        dupTablero.append(i)
    
    return dupTablero

def hayEspacioLibre(tablero, jugada):     #devuelve true si hay espacion en el tablero
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):  #permite al jugador hacer su jugada
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9 '.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('Cual es tu proxima jugada?')
        jugada = input()
    return int(jugada)

def elegirAlAzarDeLista(tablero, listaJugada):  #Devuelve una jugada válida en el tablero de la lista recibida.  Devuelve None si no hay ninguna jugada válida
    jugadasPosibles = [] 
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)

    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

def obtenerJugadaComputadora(tablero, letraComputadora):    #Dado un tablero y una letra de la computadora, determina que jugada efectuar
    if letraComputadora == 'X':
        letraJugador == 'O'
    else:
        letraJugador == 'X'
    #Algoritmo para la computadora
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i
    #verifica si el jugador puede ganar en la proxima jugada y lo bloquea
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i
    #intenta ocupar una de las esquinas si esta libre
    jugada = elegirAlAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada
    #si esta libre, ocupa el centro
    if hayEspacioLibre(tablero, 5):
        return 5
    #ocupa uno de los lados
    return elegirAlAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):  #devuelve True si cada espacio del tablero esta lleno
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

#Inicio del juego

print('Bienvenido al Ta Te Ti')

while True:
    #resetea el tablero
    elTablero = [' '] * 10

    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()

    print(turno + 'jugara primero')

    juegoEnCurso = True

    while juegoEnCurso:

        if turno == 'El jugador':   #turno del jugador
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)

            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('Felicidades, Ganaste!!!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate!')
                    break
                else:
                    turno = 'La computadora'

        else:   #turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('Lacomputadora ha ganado :(')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate')
                    break
                else:
                    turno = 'El jugador'

    if not jugarDeNuevo:
        break




