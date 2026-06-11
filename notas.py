#registro de estudiantes

estudiantes = {}
mayor_nota = 0
mayor_nombre = ""

for i in range(5):
    nombre = input("Ingrese nombre del estudiante: ")
    nota = float(input("Ingrese nota del estudiante: "))
    estudiantes[nombre] = nota
    if(nota > mayor_nota):
        mayor_nota = nota
        mayor_nombre = nombre
        
print(estudiantes)

promedio = sum(estudiantes.values()) / len(estudiantes)
print(f"El promedio del curso es {promedio}")


print(f"El estudiante con mejor promedio es: {max(estudiantes, key=estudiantes.get)}")
print(f"El estudiante con mejor promedio es: {mayor_nombre}")
