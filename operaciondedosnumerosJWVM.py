#DEFINIR VARIABLES
numero1=int()
numero2=int()
n=int()
total=float()
#DATOS DE ENTRADA
print("ingrese el primer numero")
numero1=int(input())
print("ingresse el segundo numero")
numero2=int(input())
print("la operacion que desea hacer es:1=suma,2=resta,3=multiplicacion,4=division,5=potencia")
n=int(input())
#PROCESO
if n==1:
	total=numero1+numero2
elif n==2:
	total=numero1-numero2
elif n==3:
	total=numero1*numero2
elif n==4:
	total=numero1/numero2
elif n==5:
	total=numero1**numero2
print("el resultado de la operacion es:",total)
