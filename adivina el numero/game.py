import random

intentosRealizados = 0

print("Hola, como te llamas?")
miNombre = input()

numero = random.randint(1, 20)
print('Bueno, ' + miNombre + ' estoy pensando en un numero entre el 1 y 20')

while intentosRealizados < 5:
    print('Intenta adivinar cual es, recorda que solo tenes 5 intentos')
    estimacion = input()
    estimacion = int(estimacion)
    
    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimacion es muy baja')
    if estimacion > numero:
        print('Tu estimacion es muy alta')
    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Buen trabajo,' + miNombre + 'Adivinaste en ' + intentosRealizados + ' intentos!')

if estimacion != numero:
    numero = str(numero)
    print('Que mal! no adivinaste, el numero era,' + numero)
