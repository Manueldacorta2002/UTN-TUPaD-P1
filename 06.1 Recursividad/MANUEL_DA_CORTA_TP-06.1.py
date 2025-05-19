def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales():
    hasta = int(input("Ingresá un número entero: "))
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    hasta = int(input("Ingresá la posición máxima de la serie Fibonacci: "))
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def calcular_potencia():
    base = int(input("Base: "))
    exponente = int(input("Exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

def decimal_a_binario(n):
    if n == 0:
        return ''
    return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario():
    n = int(input("Número decimal: "))
    if n == 0:
        print("0")
    else:
        print(f"Binario: {decimal_a_binario(n)}")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def verificar_palindromo():
    palabra = input("Ingresá una palabra (sin espacios ni tildes): ").lower()
    print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

def calcular_suma_digitos():
    n = int(input("Número entero positivo: "))
    print(f"Suma de dígitos: {suma_digitos(n)}")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

def calcular_bloques():
    n = int(input("Bloques en el nivel más bajo: "))
    print(f"Total de bloques: {contar_bloques(n)}")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def contar_digito_en_numero():
    numero = int(input("Número: "))
    digito = int(input("Dígito a contar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Factorial del 1 al n")
        print("2. Serie Fibonacci hasta n")
        print("3. Potencia (base^exponente)")
        print("4. Convertir decimal a binario")
        print("5. Verificar si es palíndromo")
        print("6. Sumar los dígitos de un número")
        print("7. Contar bloques en una pirámide")
        print("8. Contar dígitos en un número")
        print("9. Salir")
        opcion = input("Elegí una opción (1-9): ")

        match opcion:
            case "1":
                mostrar_factoriales()
            case "2":
                mostrar_fibonacci()
            case "3":
                calcular_potencia()
            case "4":
                convertir_a_binario()
            case "5":
                verificar_palindromo()
            case "6":
                calcular_suma_digitos()
            case "7":
                calcular_bloques()
            case "8":
                contar_digito_en_numero()
            case "9":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Probá de nuevo.")

# Ejecutar el programa
menu()
