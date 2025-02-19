precio = 5
codigo = 6

print(precio+codigo)

a = 10
b = a
a = 20

print(b)

a = 32
n = 'Daniel'
h = 1.78

print ('Edad:', a,'Nombre:', n,'Altura;', h )
print (type(a), type(n), type(h))

#listas(ejemplo las tablas del numero 8)
tablas_8 = []

for x in range(1,11):
    tablas_8.append(x * 8)

print(type(tablas_8))

for i, producto in enumerate(tablas_8, start=1):
    print(f"{i} x 8 = {producto}")

print(tablas_8)

#listas(ejemplo 2 despues de ver el video):

bandera = ['verde','blanco','rojo']

for colores in bandera:
        print(colores)

#iteracion de una cadena

nombre = 'Arturo Daniel Moncada Olvera'
nletras = 0
for indice, letra in enumerate(nombre, start=1):
    if(letra != ' '):
        print(indice, letra)

#calcular el promedio de una lista
print('Esto devuelve el promedio de una lista de numeros')
calificaciones = [7,10,6,9,8,6]
suma = sum(calificaciones)
no_cal = len(calificaciones)
promedio = (suma/no_cal)
print(f'La suma de las calificaciones es {suma} y el promedio es igual a {promedio}')
