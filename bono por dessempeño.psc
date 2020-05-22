Algoritmo bono_por_desempeñoJWVM
	//definir datos
	Definir puntos Como Entero
	definir salario ,salariominimo Como Real
	//datos de entrada
	Escribir "indique la cantidad de puntos del docente:"
	Leer puntos
	Escribir "indique su salario:"
	Leer salario
	//proceso
	salariominimo=930
	
	si puntos>=50 y puntos <=100
		total=(salariominimo*0.10)+salario
	SiNo
		si puntos>100 y puntos<=150
			total=(salariominimo*0.50)+salario
		SiNo
			total=salariominimo+salario
			
		FinSi
		
		
	FinSi
	
	Escribir "el monto del bono mas su salario sera:", total
	
FinAlgoritmo
