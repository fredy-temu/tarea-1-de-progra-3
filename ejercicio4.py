#programa que imprima el mayor y menor de una serie de 5 numeros que vamos introduciendo por teclado


def ejercicio4():
   print('programa que imprime 5 numeros mostrando el numero mayor y menor')

   a = int(input('introduzca el primer numero '))
   b = int(input('introduzca el segundo numero '))
   c = int(input('introduzca el tercer numero '))
   d = int(input('introduzca el cuarto numero '))
   e = int(input('introduzca el quinto numero '))

   if a > b and a > c and a > d and a > e:
       print('el numero mayor es el:  ' + str (a))

   elif b > a and b > c and b > d and b > e:
       print('el numero mayor es el:  ' + str (b))

   elif c > a and c > b and c>d and c > e:
       print('el numero mayor es el: ' + str (c))

   elif d > a and d > b and d > c and d > e:
       print('el numero mayor es el: ' + str (d))

   elif e > a and e > b and e > c and e > d:
       print('el numero mayor es el: ' + str (e))



ejercicio4()