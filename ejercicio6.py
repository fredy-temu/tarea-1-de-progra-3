#Calcular el factorial de un numero


def ejercicio6():


    factorial=1
    print('Dame un numero: ')
    x = eval (input())
    for i in range (1,x+1):
        factorial=factorial*i

    print(factorial)

ejercicio6()

