#Crear una lista aleatoria de 10 numeros, partiendo del numero ingresado por el usuario

def ejercicio9():

    from random import randint

    x = int(input('ingrese un numero: '))

    numeros_aleatorios = [randint(0, 100) for _ in range(9)]

    print(x, numeros_aleatorios)


ejercicio9()