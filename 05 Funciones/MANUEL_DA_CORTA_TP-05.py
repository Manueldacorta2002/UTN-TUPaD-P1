def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    return 3.14159 * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * 3.14159 * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "No se puede dividir por cero"

def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def menu():
    print("\nSelecciona un ejercicio:")
    print("1. Imprimir 'Hola Mundo'")
    print("2. Saludar al usuario")
    print("3. Mostrar información personal")
    print("4. Calcular área y perímetro de un círculo")
    print("5. Convertir segundos a horas")
    print("6. Mostrar tabla de multiplicar")
    print("7. Operaciones básicas (suma, resta, multiplicación, división)")
    print("8. Calcular IMC")
    print("9. Convertir Celsius a Fahrenheit")
    print("10. Calcular promedio de tres números")
    print("0. Salir")

while True:
    menu()
    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            imprimir_hola_mundo()
        case "2":
            nombre = input("Ingrese su nombre: ")
            print(saludar_usuario(nombre))
        case "3":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            residencia = input("Residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)
        case "4":
            radio = float(input("Ingrese el radio del círculo: "))
            print(f"Área: {calcular_area_circulo(radio):.2f}")
            print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
        case "5":
            segundos = int(input("Ingrese la cantidad de segundos: "))
            print(f"Equivalente en horas: {segundos_a_horas(segundos):.2f}")
        case "6":
            numero = int(input("Ingrese un número: "))
            tabla_multiplicar(numero)
        case "7":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            suma, resta, mult, div = operaciones_basicas(a, b)
            print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")
        case "8":
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))
            print(f"IMC: {calcular_imc(peso, altura)}")
        case "9":
            celsius = float(input("Temperatura en Celsius: "))
            print(f"Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")
        case "10":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            c = float(input("Tercer número: "))
            print(f"Promedio: {calcular_promedio(a, b, c):.2f}")
        case "0":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")
