# Realizar un programa que permita cargar dos listas de 5 valores cada una.
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
l1=0
l2=0

for x in range(5):
    n=int(input("Introduce un número de la lista 1:"))
    l1=n+l1

for x in range(5):
    n=int(input("Introduce un número de la lista 2:"))
    l2=n+l2

if (l1>l2):
    print("La prímera lista es mayor")
else:
    if (l1<l2):
        print("La segunda lista es mayor")
    else:
        print("Las listas son iguales")
    
