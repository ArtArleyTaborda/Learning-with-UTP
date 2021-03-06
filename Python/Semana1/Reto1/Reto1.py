#Un profesor debe calcular el promedio de la nota de quices de sus estudiantes para subirla a la
#plataforma de notas finales. Sn embargo, el profesor acordó con sus estudiantes que los ayudará
#eliminando la peor de las 5 notas antes de calcular el promedio que finalmente reportará.
#Adicionalmente, el profesor se ha dado cuenta qué las notas registradas en su planilla se 
#encuentran en una escala de numeros enteros de 0 a 100 pero la plataforma está diseñada para
#recibir el promedio únicamente en la escala estándar de la universidad de 0 a 5, redondeado a
#dos decimales.

#Escriba una función qué reciba cómo parámetros: una cadena con el código alfanumérico del 
#estudiante y cinco números (nota1, nota2, nota3, nota4, nota5) que representan las nota de los
#quices del semestre y retorne una cadena de ce caracteres que le proporciona al profesor la
#información que desea optener. La cadena debe tener la siguiente estructura: 
#"El promedio ajustado del estudiante {código} es: {promedio}." donde, el promedio reportado debe
#cumplir con las especificaciones mencionadas anteriormente (redondeado a dos decimales, es escala
#de 0 a 5 y calculado eliminando la peor de las cinco notas del estudiante).

#Ejemplo
#print(nota_quices("AA0010276", 19,90,38,55,68))
#El promedio ajustado del estudiante AA0010276 es: 3.14

#print(nota_quices("IS00201620", 37,10,50,19,79))
#El promedio ajustado del estudiante IS00201620 es: 2.31

#print(nota_quices("BI02201810", 45,46,33,74,22))
#El promedio ajustado del estudiante BI02201810 es: 2.48

#print(nota_quices("IQ102201810", 57,100,87,93,21))
#El promedio ajustado del estudiante IQ102201810 es: 4.21

#print(nota_quices("MA00201520", 5,14,76,91,5))
#El promedio ajustado del estudiante MA00201520 es: 2.33

#Definición de las variables globales.
notas=[]
prom=0


#Definición de la función para solicitar los datos al usuario.
def ingresar_datos(notas):
    #Ingresar los datos de las notas
   
    print("A continuación podrá ingresar las notas del estudiante ", nameStudent,"\nRecuerde por favor que el rango de las notas es de 0 a 100.")
        
    i=1
    while i <=5:
        print("Ingresa la nota",i,": ")
        n=int(input())
        if n >= 0 and n <=100:
            notas.append(n)
            i=i+1
        else:
             print("Ingresa un valor válido.")

            
    #Ordenar las notas de menor a mayor
    notas.sort()
    #Eliminar el valor mínimo
    del notas[0]


print("Este programa le ayudará a calcular el promedio de las notas de sus estudiantes.")
nameStudent = input("Por favor ingresa el nombre del estudiante: ")

ingresar_datos(notas)

suma=notas[0]+notas[1]+notas[2]+notas[3]
prom = round((suma/len(notas))/20,2)

print("El promedio ajustado del estudiante",nameStudent,"es: ",prom)