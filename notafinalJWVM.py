#DEFINIENDO VARIABLES
nota1=float()
nota2=float()
nota3=float()
nota4=float()
valnota1=float()
valnota2=float()
valnota3=float()
valnota4=float()
notafinal=float()
#DATOS DE ENTRADA
print("ingrese nota 1")
nota1 = float(input())
print("ingrese nota 2")
nota2 = float(input())
print("ingrese nota 3")
nota3 = float(input())
print("ingrese nota 4")
nota4 = float(input())
#PROCESO
valnota1=nota1*0.10
valnota2=nota2*0.15
valnota3=nota3*0.25
valnota4=nota4*0.50
notafinal=(valnota1+valnota2+valnota3+valnota4)
#DATOS DE SALIDA
print("la nota final sera:",notafinal)

