#Introducir un numero por teclado. Que nos diga si es par o impar

def ejercicio3():

    numero = input('Introduce un número que sea entero: ')
    numero = int(numero)
    if numero == 0:
        print('Este número es par ')
    elif numero % 2 == 0:
        print('Este numero es par')
    else:
        print('Este numero es impar')

ejercicio3()