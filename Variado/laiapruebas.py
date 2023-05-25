# Importamos la librería datetime para trabajar con fechas
import datetime

# Definimos el precio por hora y la cantidad de días del mes
precio_por_hora = 10.5
dias_del_mes = 30

# Pedimos al usuario los datos del servicio
nombre_servicio = input("Ingrese el nombre del servicio: ")
fecha_inicio = input("Ingrese la fecha de inicio del servicio (formato DD/MM/AAAA): ")
fecha_fin = input("Ingrese la fecha de fin del servicio (formato DD/MM/AAAA): ")
precio_servicio = float(input("Ingrese el precio del servicio: "))

# Convertimos las fechas a objetos datetime
fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
fecha_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()

# Calculamos la cantidad de días que duró el servicio
duracion = fecha_fin - fecha_inicio
dias_servicio = duracion.days + 1

# Pedimos al usuario las horas trabajadas por día y las horas extras
horas_por_dia = []
horas_extras = 0
for i in range(dias_servicio):
    horas = float(input(f"Ingrese la cantidad de horas trabajadas para el día {i+1}: "))
    horas_por_dia.append(horas)
    if horas > 8:
        horas_extras += horas - 8

# Calculamos el costo total del servicio, el costo de las horas extras y el costo total con las horas extras
costo_servicio = precio_servicio / dias_servicio
costo_horas_extras = horas_extras * (precio_por_hora * 1.5)
costo_total = precio_servicio + sum(horas_por_dia) + costo_horas_extras

# Exportamos los datos a un documento de texto
nombre_archivo = f"{nombre_servicio}_reporte.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(f"Información del servicio:\n")
    archivo.write(f"Nombre del servicio: {nombre_servicio}\n")
    archivo.write(f"Fecha de inicio: {fecha_inicio.strftime('%d/%m/%Y')}\n")
    archivo.write(f"Fecha de fin: {fecha_fin.strftime('%d/%m/%Y')}\n")
    archivo.write(f"Precio del servicio: ${precio_servicio}\n\n")
    
    archivo.write(f"Horas trabajadas por día:\n")
    for i in range(dias_servicio):
        archivo.write(f"Día {i+1}: {horas_por_dia[i]} horas\n")
    archivo.write("\n")
    
    archivo.write(f"Costo por día del servicio: ${costo_servicio}\n")
    archivo.write(f"Total de horas extras: {horas_extras} horas\n")
    archivo.write(f"Costo por horas extras: ${costo_horas_extras}\n\n")
    
    archivo.write(f"Costo total del servicio: ${costo_total}")
    
print(f"El reporte se ha generado exitosamente en el archivo {nombre_archivo}")