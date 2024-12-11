# Cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares.
p=0
im=0
n=int(input("Introduce el número de elementos a leer:"))
for x in range(n):
    nu=int(input("Introduce un número:"))
    if (nu%==0):
        p=p+1
    else:
        im=im+1
print("Pares:",p)
print("Impares:",im)
