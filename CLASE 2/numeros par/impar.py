num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos números son pares.")
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("Al menos uno de los números es par.")
else:
    print("Ninguno de los números es par.")
