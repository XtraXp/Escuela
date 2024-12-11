# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
# realizar un programa que lea los sueldos que cobra cada empleado e
# informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa
# deberá informar el importe que gasta la empresa en sueldos al personal.
suma=0
ma=0
me=0
n=int(input("¿Cuantos trabajadores estan contratados? "))
for x in range(n):
    sueldo=float(input("Introduzca un sueldo "))
    suma=suma+sueldo
    if sueldo>300:
        ma=ma+1
    else:
        me=me+1
print("Hay", me, "empleados cobrando menos de 300$, y", ma, "cobrando más de 300$")
print("El total de dinero que pagara la empresa sera de", suma)
