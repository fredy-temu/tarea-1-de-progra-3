#Realizar la tabla de multiplicar de un numero entre 0 y 10

def ejercicio8():

    numero = int(input('ingrese un numero entero '))

    for i in range(0, 11):
        print(f'{numero} * {i} = {numero * i}')


ejercicio8()