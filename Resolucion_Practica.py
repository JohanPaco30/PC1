#RESOLUCION DE LOS PROBLEMAS DE LA PRACTICA 1:

"""
Problema 1:
Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
usuario haya introducido.
"""
username = input("Introduzca su nombre de usuario: ")
print("¡Hola " + str(username) + "!")

"""
Problema 2:
En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.
"""
cuenta = float(input("¿Cuánto gastó en el restaurante?: "))
porcentaje = int(input("¿Algún porcentaje de propina para el mesero?: "))
propina = cuenta * (porcentaje/100)

print("La cantidad de propina a dejar al mesero de acuerdo a su consumo es: " + str(propina))

"""
Problema 3:
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""
numero_payasos = int(input("Cantidad de payasos vendidos: "))
numero_munecas = int(input("Cantidad de muñecas vendidos: "))
peso_paquete = (numero_payasos*112) + (numero_munecas*75)

print("El peso total del paquete enviado será: " + str(peso_paquete) + " g")

"""
Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N.
"""
numero = int(input("Introduzca un numero entero: "))
suma_n = (numero*(numero + 1))/2

print("La suma de los N primeros enteros es: " + str(suma_n))

"""
Problema 5:
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.
"""

shows_m = int(input("¿Cuántos shows musicales ha visto este año?: "))

if shows_m > 3:
    print("True")
else:
    print("False")


"""
Problema 6:
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.
"""

edad_cliente = int(input("¿Cuantos años tiene?: "))

if edad_cliente < 4:
    print("¡INGRESO GRATIS!")
elif edad_cliente >= 4 and edad_cliente <= 18:
    print("MONTO A PAGAR DE: $5")
else:
    print("MONTO A PAGAR DE: $10")

"""
Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))

suma = num_1 + num_2
resta = num_1 - num_2
multi = num_1 * num_2

print("¿Qué desea hacer?:\n1) Mostrar una suma de los dos números.\n2) Mostrar una resta de los dos números (el primero menos el segundo).\n3) Mostrar una multiplicación de los dos números.")
opcion = int(input("Elige una opcion: "))

if opcion == 1:
    print("La suma de los dos numeros es: " + str(suma ))
elif opcion == 2:
    print("La resta de los dos numeros es: " + str(resta))
elif opcion ==3:
    print("El producto de los dos numeros es: " + str(multi))

"""
Problema 8:
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00. Implemente un programa que solicite 
al usuario una hora y le indique si es la hora del desayuno, la hora del almuerzo o la hora de la cena. 
Si no es hora de comer, no envíes nada.

Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
"""

horario= (input("Introduzca la hora actual: "))
hora, minutos = horario.split(":")
hora = int(hora)

if hora >= 7 and hora <= 8:
    print("¡Es la hora del desayuno!")
elif hora >= 12 and hora <= 13:
    print("¡Es la hora del almuerzo!")
elif hora >= 18 and hora <= 19:
        print("¡Es la hora de la cena!")

"""
Problema 9:
Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
'día', 'buen', 'Di'].
"""

lista_1= ['A','M','A','N','A','P','A','N','A','M','A']
lista_1.reverse()

print("Sabias que la frase 'AMAN A PANAMA' suena igual si la escribes al reves:\n")
print(lista_1)
print("\nCuriosamente suena igual.")

"""
Problema 10:
Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']
"""

lista_2 = ['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
lista_2.remove('Rojo')
lista_2.remove('Rosa')
lista_2.remove('Amarillo')
print(lista_2)

"""
Problema 11:
Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,, 5]
"""

lista_3 = [1,1,2,3,4,4,5,1]
lista_3.remove(1)
lista_3.remove(1)
lista_3.remove(4)
lista_3.sort()

print(lista_3)

"""
Problema 12:
Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip
Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.
"""

archivo = input("Introduzca el nombre del archivo con su extension correspondiente (¡No usar Mayúsculas!) ")

if archivo[-3:] == "gif":
    print("El tipo MIME del archivo " + archivo + " es: image/gif")
elif archivo[-3:] == "jpg":
     print("El tipo MIME del archivo " + archivo + " es: image/jpeg")
elif archivo[-4:] == "jpeg":
      print("El tipo MIME del archivo " + archivo + " es: image/jpeg")
elif archivo[-3:] == "png":
      print("El tipo MIME del archivo " + archivo + " es: image/png")
elif archivo[-3:] == "pdf":
      print("El tipo MIME del archivo " + archivo + " es: application/pdf")
elif archivo[-3:] == "txt":
    print("El tipo MIME del archivo " + archivo + " es: text/plain")
elif archivo[-3:] == "zip":
      print("El tipo MIME del archivo " + archivo + " es: application/zip")
else:
     print("El tipo MIME del archivo " + archivo + " es: application/octet-stream")

