#Realizar un programa que lea cuatro valores numéricos e
#informar su suma y promedio.
n1=int(input("Escribe número:"))
if(n1<0):
    print("¡Debes poner un número positivo!")
else:
    if(n1<10):
        print ("El número tiene un dígito")
    else:
        if(n1<100):
            print ("El número tiene dos dígitos")
        else:
            if(n1<10000000000000000):
                print ("El número tiene más de dos dígitos")
