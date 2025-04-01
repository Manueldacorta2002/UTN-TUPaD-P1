import math

def ejercicio_1():
    print("Hola Mundo!")

def ejercicio_2():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola {nombre}!")

def ejercicio_3():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def ejercicio_4():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print(f"El área del círculo es {area:.2f} y su perímetro es {perimetro:.2f}.")

def ejercicio_5():
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

def ejercicio_6():
    numero = int(input("Ingresa un número: "))
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def ejercicio_7():
    num1 = int(input("Ingresa el primer número entero (distinto de 0): "))
    num2 = int(input("Ingresa el segundo número entero (distinto de 0): "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2:.2f}")

def ejercicio_8():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    IMC = peso / (altura ** 2)
    print(f"Tu índice de masa corporal (IMC) es {IMC:.2f}.")

def ejercicio_9():
    temperatura_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temperatura_fahrenheit = (9/5) * temperatura_celsius + 32
    print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit:.2f}°F.")

def ejercicio_10():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los tres números es {promedio:.2f}.")

ejercicios = {
    1: ejercicio_1,
    2: ejercicio_2,
    3: ejercicio_3,
    4: ejercicio_4,
    5: ejercicio_5,
    6: ejercicio_6,
    7: ejercicio_7,
    8: ejercicio_8,
    9: ejercicio_9,
    10: ejercicio_10
}

while True:
    try:
        seleccion = int(input("Seleccione el ejercicio a evaluar (1-10) o 0 para salir: "))
        if seleccion == 0:
            print("Saliendo del programa...")
            break
        elif seleccion in ejercicios:
            ejercicios[seleccion]()
        else:
            print("Número de ejercicio inválido. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
