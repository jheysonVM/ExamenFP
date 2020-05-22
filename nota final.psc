Algoritmo nota_final_JWVM
	//definir datos
	Definir nota1,nota2,nota3,nota4 ,notafinal como real
	definir valnota1,valnota2,valnota3 ,valnota4 Como real
	//datos de entrada
	Escribir "ingrese nota 1"
	Leer nota1
	Escribir "ingrese nota 2"
	Leer nota2
	Escribir "ingrese nota 3"
	Leer nota3
	Escribir "ingrese nota 4"
	leer nota4
	//proceso
	valnota1=nota1*0.10
	valnota2=nota2*0.15
	valnota3=nota3*0.25
	valnota4=nota4*0.50
	notafinal=(valnota1+valnota2+valnota3+valnota4)
	
	//datos de salida
	Escribir "la nota final sera:",notafinal
	
	
FinAlgoritmo
