# LISTAS
numeros = [3, 7, 2, 8, 5]
print("Primer número:", numeros[0])
print("Último número:", numeros[-1])
numeros.append(10)
print("Lista después de agregar 10:", numeros)

# WHILE
contador = 1
while contador <= 5:
    print("Contador:", contador)
    contador += 1

# FOR
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print("Me gusta la", fruta)

# FUNCIONES
def suma(a, b):
    return a + b

resultado = suma(4, 6)
print("La suma es:", resultado)
