from Funciones import *

#EJERCICIO 1

nombre=pedir_texto("Ingrese su nombre y apellido: ")
edad=pedir_entero("Ingrese su edad: ",18,120)
promedio_general=pedir_float("Ingrese el promedio general: ")
ingresos_familiares=("No aplica")

if promedio_general<=5:
    resultado=("Rechazado")
else:
    ingresos_familiares=pedir_float("Indique los ingresos familiares mensuales: ")
    if ingresos_familiares<300000:
        resultado=("Beca completa")
    elif ingresos_familiares>=300000 and ingresos_familiares<=600000:
        resultado=("Media beca")
    elif ingresos_familiares>600000:
        resultado=("Rechazado")
    else: 
        pass

print(f"{nombre},{edad} años")      
print(f"Promedio: {promedio_general}")
print(f"Ingresos: ${ingresos_familiares}")
print(f"Resultado: {resultado}")


#EJERCICIO 2

nombre=pedir_texto("Ingrese su nombre completo: ")
dni=pedir_entero("Ingrese su DNI: ")
edad=pedir_entero("Ingrese su edad: ",0,120)
obra_social=pedir_texto("Obra social (SI/NO): ")
prioridad=pedir_entero("1=Emergencia, 2=Urgente, 3=Control: ")
obra_minusculas=obra_social.lower()

if prioridad==1:
    turno=("Inmediatamente a guardia.")
    exit()
elif prioridad==2:
    if obra_social=="si":
        turno=("Turno en menos de 24hs.")
    else:
        turno=("Turno en 48hs.")
elif prioridad==3:
    if edad>65:
        turno=("Turno preferencial en 72hs.")
    else:
        turno=("Turno normal en 7 dias.")

print(f"Paciente: {nombre}")
print(f"DNI: {dni}")
print(f"Edad: {edad}")
print(f"Prioridad: {prioridad}")
print(f"Turno asignado: {turno}")

#EJERCICIO 3

nombre_apellido=""
cuit=0
ingresos_mensuales=0
antiguedad=0
historial=""

nombre_apellido=pedir_texto("Ingrese su nombre y apellido: ")
cuit=pedir_cuit("Ingrese su CUIT: ")
ingresos_mensuales=pedir_entero("Indique sus ingresos mensuales: ")
antiguedad=pedir_entero("Ingrese su antigüedad laboral (años): ")
historial=pedir_texto("Indique su historial crediticio (bueno/regular/malo): ")
historial_minus=historial.lower()
condicion=""

if historial_minus=="malo":
    condicion=("Rechazado.")
else:
    if ingresos_mensuales<200_000:
        condicion=("Rechazado.")
    elif ingresos_mensuales>=200_000 and antiguedad<2:
        condicion=("Puede pedir hasta $500.000")
    elif ingresos_mensuales>=200_000 and antiguedad>=2:
        if historial_minus==("regular"):
            condicion=("Puede pedir hasta $1.000.000")
        elif historial_minus==("bueno"):
            condicion=("Puede pedir hasta $3.000.000")
        else:
            print("Ingrese su historial correctamente.")
            exit()

print(f"Cliente: {nombre_apellido}")
print(f"CUIT: {cuit}")
print(f"Ingresos: {ingresos_mensuales}")
print(f"Antigüedad: {antiguedad} años")
print(f"Historial: {historial}")
print(f"Monto aprobado: {condicion}")


#EJERCICIO 1 (EN CASA) #TERMINAR

imp_mayor=0.35
imp_medio=0.2
imp_menor=0.1
limite_edad=65
nombre_completo=""
edad=0
ingresos_anuales=0

nombre_completo=pedir_texto("Ingresar su nombre completo: ")
edad=pedir_entero("Ingresar su edad: ",18,120)
ingresos_anuales=pedir_entero("Ingrese el total de sus ingresos anuales: ",0)

if ingresos_anuales<500_000:
    print("No paga impuestos")
    impuesto_final=0
elif ingresos_anuales>=500_000 and ingresos_anuales<2_000_000:
    if edad>=limite_edad:
        print("Paga ",imp_menor/2,"% de impuestos")
        impuesto_final=ingresos_anuales*(imp_menor/100)
    else:
        print("Paga",imp_menor"% de impuestos")
        impuesto_final=ingresos_anuales*(imp_menor/100)
elif ingresos_anuales

#EJERCICIO 2 (EN CASA)

nombre=""
legajo=0
nota1=0
nota2=0
nota3=0
condicion=""

nombre=pedir_texto("Ingrese nombre y apellido: ")
legajo=pedir_entero("Ingrese su legajo: ")
nota1=pedir_entero("Ingrese su primer nota: ",0,10)
nota2=pedir_entero("Ingrese su segunda nota: ",0,10)
nota3=pedir_entero("Ingrese su tercera nota: ",0,10)

promedio=(nota1+nota2+nota3)/3

if nota1<4 or nota2<4 or nota3<4:
    condicion=("Desaprobado directo")
elif promedio<6:
    condicion=("Desaprobado")
elif promedio>=6 and promedio<=7:
    condicion=("Aprobado con final")
elif promedio>=8:
    condicion=("Promocionado")

print(f"Nombre: {nombre}")
print(f"Legajo: {legajo}")
print(f"Estado académico final: {condicion}")