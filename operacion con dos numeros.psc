Algoritmo operaion_de_dos_numerosJWVM
	//DEFINIR DATOS
	
	definir numero1,numero2,n Como Entero
	//datos de entrada
	Escribir "ingrese el primer numero"
	Leer numero1
	Escribir "ingrese el segundo numero"
	Leer numero2
	Escribir "la operaciona realizar es;1=suma;2=resta;3=multiplicacion;4=division;5=potencia:"
	Leer n
	Segun n hacer
		1:
			total=numero1+numero2
		2:
			total=numero1-numero2
		3:
			total=numero1*numero2
		4:
			total=numero1/numero2
		5:
			total=numero1^numero2
	FinSegun
	
	Escribir "el resultado de la operacion es :",total
	
FinAlgoritmo
