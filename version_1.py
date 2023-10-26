
import  math 

print("Bienvenido a nuestra calculadora Zellers Congruence V_1")


fecha = input("Ingresa una fecha con este formato dia/mes/año:  ")

dia, mes, anio = map(int, fecha.split("/"))

if mes == 1 or mes == 2:
    mes += 12
    anio -= 1

k =  anio % 100
j =  anio // 100

# Aplicar la fórmula Zeller's Congruence
h = (dia + math.floor(13 * (mes + 1) / 5) + k + math.floor(k / 4) + math.floor(j / 4) - 2 * j) % 7

dia_semana = ["Sabado", "Domingo", "Lunes", "Martes", "Miercóles", "Jueves", "Viernes"]

print(dia_semana[h])