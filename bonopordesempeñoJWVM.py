#DEFINIR VARIABLES
puntos= int()
salario= float()
#DATOS DE ENTRADA
print("indique la cantidad de puntos del docente")
puntos = int(input())
print("indique su salario")
salario = float(input())
#PROCESO
salariominimo=930
if puntos>50 and puntos<=100:
    total=(salariominimo*0.10)+salario
else:
    if puntos>100 and puntos<=150:
        total=(salariominimo*0.50)+salario
    else:
        total=salariominimo+salario

print("el monto del bono mas su salario es de :",total)           
        