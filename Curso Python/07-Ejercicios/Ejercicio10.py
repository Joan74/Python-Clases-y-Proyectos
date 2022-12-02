"""
Crear un programa que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han supendido.
"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("introduce la cantidad de alumnos: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota le pones al \"alumno: {contador}\"? "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1

print(f"Alumnos Aprobados: {aprobados}")
print(f"Alimnos suspendidos: {suspendidos}")
