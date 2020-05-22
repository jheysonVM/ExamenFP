#DEFINIR VARIABLES
a=int
#DATOS DE ENTRADA
print("ingrese laedad del paciente")
a= int(input())
#PROCESO
if a>70:
    print("se debe aplicar la vacuna tipo C")
else: 
    if a>=16 and a<=70:
        print("si es mujer aplicar vacuna tipo B")
        print("si es varon aplicar vacuna tipo A")
    else:
        print("debe aplicar vacuna tipo A")

