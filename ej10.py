import string


def promedio_mas_alto(dicc_p):
    alumno_p_a = ""
    promedio_max = float(-1)
    for alumno in dicc_p:
        #print(f"{alumno}, nota: {dicc_p[alumno]}")
        if dicc_p[alumno] > promedio_max:
            alumno_p_a = alumno
            promedio_max = dicc_p[alumno]
    
    return alumno_p_a

def promedio_mas_bajo(dicc_p):
    alumno_p_b = ""
    promedio_min = float(999)
    for alumno in dicc_p:
        #print(f"{alumno}, nota: {dicc_p[alumno]}")
        if dicc_p[alumno] < promedio_min:
            alumno_p_b = alumno
            promedio_min = dicc_p[alumno]
    
    return alumno_p_b


def calcular_promedio(dicc):
    dicc_p = {}
    for alumno in dicc:
        nota_1 = dicc[alumno][0]
        nota_2 = dicc[alumno][1]
        dicc_p[alumno] = round(((nota_1 + nota_2) / float(2)), 2)
    
    return dicc_p

def armar_estructura(dicc, nombres, notas_1, notas_2):
    
    for alumno in range(len(nombres)):
        dicc[nombres[alumno]] = [notas_1[alumno], notas_2[alumno]]
    
    return dicc
    


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

nombres = nombres.split(",")
for elem in range(len(nombres)):
    nombres[elem] = nombres[elem].strip()
    nombres[elem] = nombres[elem].strip("'")
    
dicci_alumnos = {}
dicci_promedios = {}

armar_estructura(dicci_alumnos, nombres, notas_1, notas_2)

dicci_promedios = calcular_promedio(dicci_alumnos)
alumno_promedio_alto = promedio_mas_alto(dicci_promedios)
alumno_promedio_bajo = promedio_mas_bajo(dicci_promedios)

print(dicci_alumnos)
print(dicci_promedios)
print(f"El alumno con promedio mas alto es {alumno_promedio_alto}")
print(f"El alumno con promedio mas bajo es {alumno_promedio_bajo}")
