# Realizar un programa que solicite la carga por teclado de dos números,
# si el primero es mayor al segundo informar su suma y diferencia,
# en caso contrario informar el producto y la división del primero
# respecto al segundo.
n1=int(input("Escribe número 1:"))
n2=int(input("Escribe número 2:"))
if(n1>n2):
    suma=n1+n2
    resta=n1-n2
    print("La suma entre el primer y segundo número es de", suma)
    print("La resta entre el primer y segundo número es de", resta)
else:
    producto=n1*n2
    division=n1/n2
    print("El producto entre el primer y segundo número es de", producto)
    print("La división entre el primer y segundo número es de", division)

