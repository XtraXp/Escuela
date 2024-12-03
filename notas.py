# Se ingresan tres notas de un alumno,
# si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado".
n1=int(input("Escribe nota 1:"))
n2=int(input("Escribe nota 2:"))
n3=int(input("Escribe nota 3:"))
media=(n1+n2+n3)/3
if(media>7):
    print("El alumno ha promocionado")
else:
    print("El alumno no ha promocionado")
