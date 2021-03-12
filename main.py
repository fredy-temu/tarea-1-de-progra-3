#Hacer un programa que imprima los numeros impares hasta el 100 y que imprima cuantos impares hay

def ejercicio1():
limite = 10
indice=1
indice2=0

while indice <=limite:
    if indice % 2:
        print('es impar - indice = ' + str(indice))
        indice2+=1
    indice+=1

 print('total de numeros impares =' + str(indice2))