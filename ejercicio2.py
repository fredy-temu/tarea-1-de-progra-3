#Hacer un programa que solo nos permita introducir S o N

def ejercicio2():
    letra = input('ingrese una letra ')
    if letra == 'S':
        print('la letra ingresada es VALIDA: ' + str(letra))
    elif letra == 'N':
        print('la letra ingresada es VALIDA: ' + str(letra))
    else:
        print('la letra ingresada NO ES PERMITIDA ')


ejercicio2()