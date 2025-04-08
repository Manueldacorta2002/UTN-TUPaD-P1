def ejercicio1():
    for i in range(101):
        print(i)

def ejercicio2():
    num = input("Ingrese un número entero: ")
    print("Cantidad de dígitos:", len(num))

def ejercicio3():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    menor = min(a, b) + 1
    mayor = max(a, b)
    suma = sum(range(menor, mayor))
    print("La suma entre esos valores es:", suma)

def ejercicio4():
    total = 0
    while True:
        n = int(input("Ingrese un número (0 para terminar): "))
        if n == 0:
            break
        total += n
    print("Total acumulado:", total)

def ejercicio5():
    import random
    secreto = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el número (entre 0 y 9): "))
        intentos += 1
        if intento == secreto:
            print(f"¡Correcto! Lo lograste en {intentos} intento(s).")
            break

def ejercicio6():
    for i in range(100, -1, -2):
        print(i)

def ejercicio7():
    n = int(input("Ingrese un número entero positivo: "))
    suma = sum(range(n + 1))
    print("La suma desde 0 hasta", n, "es:", suma)

def ejercicio8():
    pares = impares = positivos = negativos = 0
    cantidad = int(input("¿Cuántos números vas a ingresar? "))
    for _ in range(cantidad):
        n = int(input("Número: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
        if n >= 0:
            positivos += 1
        else:
            negativos += 1
    print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

def ejercicio9():
    cantidad = int(input("¿Cuántos números vas a ingresar? "))
    total = 0
    for _ in range(cantidad):
        n = int(input("Número: "))
        total += n
    print("La media es:", total / cantidad)

def ejercicio10():
    num = input("Ingrese un número: ")
    print("Número invertido:", num[::-1])

def menu():
    while True:
        print("""
        --- MENÚ DE EJERCICIOS ---
        1. Imprimir del 0 al 100
        2. Contar dígitos de un número
        3. Sumar entre dos números (sin incluirlos)
        4. Suma secuencial hasta ingresar 0
        5. Juego de adivinanza (0 a 9)
        6. Números pares del 100 al 0
        7. Suma de 0 hasta número ingresado
        8. Clasificar números (pares/impares, positivos/negativos)
        9. Media de N números
        10. Invertir un número
        0. Salir
        """)
        opcion = int(input("Elija una opción: "))
        match opcion:
            case 1: ejercicio1()
            case 2: ejercicio2()
            case 3: ejercicio3()
            case 4: ejercicio4()
            case 5: ejercicio5()
            case 6: ejercicio6()
            case 7: ejercicio7()
            case 8: ejercicio8()
            case 9: ejercicio9()
            case 10: ejercicio10()
            case 0: 
                print("¡Nos vemos!")
                break
            case _: print("Opción no válida.")

menu()
