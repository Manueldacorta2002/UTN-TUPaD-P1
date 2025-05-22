import random
import time



# Ejercicio 1: Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Ejercicio 2: Búsqueda lineal contando comparaciones
def busqueda_lineal_contando(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            print(f"Número de comparaciones realizadas: {comparaciones}")
            return i
    print(f"Número de comparaciones realizadas: {comparaciones}")
    return -1

# Ejercicio 3: Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejercicio 4: Búsqueda binaria contando pasos
def busqueda_binaria_contando(lista, objetivo):
    pasos = 0
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            print(f"Número de pasos realizados: {pasos}")
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print(f"Número de pasos realizados: {pasos}")
    return -1

# Ejercicio 5: Genera lista aleatoria y búsqueda lineal
def ejercicio_5_logica(): # Función auxiliar para la lógica del ejercicio 5
    lista = [random.randint(1, 100) for _ in range(20)] [cite: 14]
    print("Lista generada:", lista) [cite: 14]

    indice = busqueda_lineal(lista, 50) [cite: 13]
    if indice != -1:
        print(f"El número 50 se encontró en el índice: {indice}")
    else:
        print("El número 50 no se encontró en la lista.")

# Ejercicio 6: Ordena lista y búsqueda binaria
def ejercicio_6_logica(): # Función auxiliar para la lógica del ejercicio 6
    lista = [random.randint(1, 100) for _ in range(20)] # Generamos una nueva lista para que el ejercicio sea independiente
    lista_ordenada = sorted(lista) [cite: 15]
    print("Lista ordenada:", lista_ordenada) [cite: 15]

    indice = busqueda_binaria(lista_ordenada, 50) [cite: 15]
    if indice != -1:
        print(f"El número 50 se encontró en el índice: {indice}")
    else:
        print("El número 50 no se encontró en la lista ordenada.")

# Ejercicio 7: Contar ocurrencias
def contar_ocurrencias(lista, numero):
    count = 0
    for elemento in lista:
        if elemento == numero:
            count += 1
    return count

# Ejercicio 8: Comparación de tiempo entre búsqueda lineal y binaria
def ejercicio_8_logica(): # Función auxiliar para la lógica del ejercicio 8
    lista_grande = list(range(10000)) [cite: 18]

    print("Realizando búsqueda lineal...")
    inicio_lineal = time.time() [cite: 17]
    busqueda_lineal(lista_grande, 9999) # Buscar el último elemento para ver el peor caso en búsqueda lineal
    fin_lineal = time.time() [cite: 17]
    tiempo_lineal = fin_lineal - inicio_lineal
    print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")

    print("Realizando búsqueda binaria...")
    inicio_binaria = time.time() [cite: 17]
    busqueda_binaria(lista_grande, 9999) # Buscar el último elemento para ver cómo se comporta la búsqueda binaria
    fin_binaria = time.time() [cite: 17]
    tiempo_binaria = fin_binaria - inicio_binaria
    print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.6f} segundos")

# Ejercicio 9: Buscar en diccionario por valor (edad)
def buscar_por_edad(diccionario, edad):
    for nombre, ed_valor in diccionario.items():
        if ed_valor == edad:
            return nombre
    return "No encontrado"



def test_ejercicio_1():
    print("\n--- Ejercicio 1: Búsqueda Lineal ---")
    lista_ej1 = [10, 20, 30, 40, 50] [cite: 6]
    print(f"Lista: {lista_ej1}, Objetivo: 30") [cite: 6]
    print(f"Índice encontrado: {busqueda_lineal(lista_ej1, 30)}") [cite: 6]

def test_ejercicio_2():
    print("\n--- Ejercicio 2: Búsqueda Lineal Contando Comparaciones ---")
    lista_ej2 = [10, 20, 30, 40, 50] [cite: 8]
    print(f"Lista: {lista_ej2}, Objetivo: 50") [cite: 7]
    busqueda_lineal_contando(lista_ej2, 50) [cite: 7, 8]

def test_ejercicio_3():
    print("\n--- Ejercicio 3: Búsqueda Binaria ---")
    lista_ej3 = [1, 3, 5, 7, 9, 11, 13, 15] [cite: 10]
    print(f"Lista: {lista_ej3}, Objetivo: 7") [cite: 10]
    print(f"Índice encontrado: {busqueda_binaria(lista_ej3, 7)}") [cite: 9, 10]

def test_ejercicio_4():
    print("\n--- Ejercicio 4: Búsqueda Binaria Contando Pasos ---")
    lista_ej4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] [cite: 12]
    print(f"Lista: {lista_ej4}, Objetivo: 11") [cite: 11]
    busqueda_binaria_contando(lista_ej4, 11) [cite: 11, 12]

def test_ejercicio_7():
    print("\n--- Ejercicio 7: Contar Ocurrencias ---")
    lista_ej7 = [1, 5, 2, 5, 3, 5, 4, 5] [cite: 16]
    print(f"Lista: {lista_ej7}, Número a contar: 5") [cite: 16]
    print(f"El número 5 aparece {contar_ocurrencias(lista_ej7, 5)} veces.") [cite: 16]

def test_ejercicio_9():
    print("\n--- Ejercicio 9: Búsqueda en Diccionario por Valor ---")
    personas_ej9 = {"Alice": 25, "Bob": 30, "Charlie": 22} [cite: 21]
    print(f"Diccionario: {personas_ej9}, Edad a buscar: 30") [cite: 20]
    print(f"Nombre asociado a la edad 30: {buscar_por_edad(personas_ej9, 30)}") [cite: 20, 21]


# Función principal para el "switch" de ejercicios
def main():
    exercises = {
        '1': test_ejercicio_1,
        '2': test_ejercicio_2,
        '3': test_ejercicio_3,
        '4': test_ejercicio_4,
        '5': ejercicio_5_logica,
        '6': ejercicio_6_logica,
        '7': test_ejercicio_7,
        '8': ejercicio_8_logica,
        '9': test_ejercicio_9,
    }

    while True:
        print("\n--- Menú de Ejercicios ---")
        print("1) Búsqueda lineal")
        print("2) Búsqueda lineal contando comparaciones")
        print("3) Búsqueda binaria")
        print("4) Búsqueda binaria contando pasos")
        print("5) Búsqueda lineal con lista aleatoria")
        print("6) Búsqueda binaria con lista ordenada")
        print("7) Contar ocurrencias")
        print("8) Comparación de tiempos de búsqueda")
        print("9) Búsqueda en diccionario por edad")
        print("q) Salir")

        choice = input("Seleccione el ejercicio a ejecutar (1-9) o 'q' para salir: ").strip().lower()

        if choice == 'q':
            print("Saliendo del programa.")
            break
        elif choice in exercises:
            exercises[choice]() # Llama a la función asociada directamente
        else:
            print("Elección inválida. Por favor, ingrese un número del 1 al 9 o 'q'.")

if __name__ == "__main__":
    main()