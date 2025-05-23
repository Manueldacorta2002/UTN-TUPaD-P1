import random
import time

# Ejercicio 1: Búsqueda lineal
def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en la lista para encontrar el objetivo.
    Retorna el índice del objetivo si se encuentra, de lo contrario -1.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Ejercicio 2: Búsqueda lineal contando comparaciones
def busqueda_lineal_contando(lista, objetivo):
    """
    Realiza una búsqueda lineal y cuenta el número de comparaciones.
    Retorna el índice del objetivo si se encuentra, de lo contrario -1.
    """
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1 # Cada vez que se accede a un elemento para comparar
        if lista[i] == objetivo:
            print(f"Número de comparaciones realizadas: {comparaciones}")
            return i
    print(f"Número de comparaciones realizadas: {comparaciones}")
    return -1

# Ejercicio 3: Búsqueda binaria
def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada para encontrar el objetivo.
    Retorna el índice del objetivo si se encuentra, de lo contrario -1.
    """
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
    """
    Realiza una búsqueda binaria y cuenta el número de pasos (iteraciones).
    Retorna el índice del objetivo si se encuentra, de lo contrario -1.
    """
    pasos = 0
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        pasos += 1 # Cada iteración del bucle es un "paso"
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

# Ejercicio 7: Contar ocurrencias
def contar_ocurrencias(lista, numero):
    """
    Cuenta cuántas veces aparece un número específico en una lista.
    """
    count = 0
    for elemento in lista:
        if elemento == numero:
            count += 1
    return count

# Ejercicio 9: Buscar en diccionario por valor (edad)
def buscar_por_edad(diccionario, edad):
    """
    Busca una edad específica en los valores de un diccionario y retorna
    la clave (nombre) asociada si la encuentra. Retorna "No encontrado" si no.
    """
    for nombre, ed_valor in diccionario.items():
        if ed_valor == edad:
            return nombre
    return "No encontrado"

# --- FUNCIONES AUXILIARES PARA EJECUTAR LOS EJERCICIOS ---

def ejercicio_5_logica():
    """
    Lógica para el Ejercicio 5: Genera lista aleatoria y realiza búsqueda lineal.
    """
    print("Generando lista aleatoria de 20 números entre 1 y 100...")
    lista = [random.randint(1, 100) for _ in range(20)]
    print("Lista generada:", lista)

    print("\nBuscando el número 50 en la lista...")
    indice = busqueda_lineal(lista, 50)
    if indice != -1:
        print(f"El número 50 se encontró en el índice: {indice}")
    else:
        print("El número 50 no se encontró en la lista.")

def ejercicio_6_logica():
    """
    Lógica para el Ejercicio 6: Genera lista aleatoria, la ordena y realiza búsqueda binaria.
    """
    print("Generando lista aleatoria de 20 números entre 1 y 100...")
    lista = [random.randint(1, 100) for _ in range(20)]
    lista_ordenada = sorted(lista) 
    print("Lista original (sin ordenar):", lista)
    print("Lista ordenada:", lista_ordenada)

    print("\nBuscando el número 50 en la lista ordenada...")
    indice = busqueda_binaria(lista_ordenada, 50)
    if indice != -1:
        print(f"El número 50 se encontró en el índice: {indice}")
    else:
        print("El número 50 no se encontró en la lista ordenada.")

def ejercicio_8_logica():
    """
    Lógica para el Ejercicio 8: Compara el tiempo de ejecución entre búsqueda lineal y binaria.
    """
    print("Generando una lista grande (10,000 elementos) para la comparación...")
    lista_grande = list(range(10000)) 

    print("\n--- Realizando búsqueda lineal ---")
    objetivo_lineal = 9999 
    inicio_lineal = time.time()
    pos_lineal = busqueda_lineal(lista_grande, objetivo_lineal)
    fin_lineal = time.time()
    tiempo_lineal = fin_lineal - inicio_lineal
    print(f"Elemento {objetivo_lineal} encontrado en índice: {pos_lineal}" if pos_lineal != -1 else f"Elemento {objetivo_lineal} no encontrado.")
    print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")

    print("\n--- Realizando búsqueda binaria ---")
    objetivo_binaria = 9999 
    inicio_binaria = time.time()
    pos_binaria = busqueda_binaria(lista_grande, objetivo_binaria)
    fin_binaria = time.time()
    tiempo_binaria = fin_binaria - inicio_binaria
    print(f"Elemento {objetivo_binaria} encontrado en índice: {pos_binaria}" if pos_binaria != -1 else f"Elemento {objetivo_binaria} no encontrado.")
    print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.6f} segundos")



def test_ejercicio_1():
    print("\n--- Ejecutando Ejercicio 1: Búsqueda Lineal ---")
    lista_ej1 = [10, 20, 30, 40, 50]
    objetivo_ej1 = 30
    print(f"Lista: {lista_ej1}, Objetivo: {objetivo_ej1}")
    indice = busqueda_lineal(lista_ej1, objetivo_ej1)
    if indice != -1:
        print(f"El objetivo {objetivo_ej1} se encontró en el índice: {indice}")
    else:
        print(f"El objetivo {objetivo_ej1} no se encontró en la lista.")
    
    objetivo_no_encontrado = 99
    print(f"\nLista: {lista_ej1}, Objetivo: {objetivo_no_encontrado}")
    indice_no_e = busqueda_lineal(lista_ej1, objetivo_no_encontrado)
    if indice_no_e != -1:
        print(f"El objetivo {objetivo_no_encontrado} se encontró en el índice: {indice_no_e}")
    else:
        print(f"El objetivo {objetivo_no_encontrado} no se encontró en la lista.")

def test_ejercicio_2():
    print("\n--- Ejecutando Ejercicio 2: Búsqueda Lineal Contando Comparaciones ---")
    lista_ej2 = [10, 20, 30, 40, 50]
    objetivo_ej2 = 50
    print(f"Lista: {lista_ej2}, Objetivo: {objetivo_ej2}")
    indice = busqueda_lineal_contando(lista_ej2, objetivo_ej2)
    if indice != -1:
        print(f"El objetivo {objetivo_ej2} se encontró en el índice: {indice}")
    else:
        print(f"El objetivo {objetivo_ej2} no se encontró en la lista.")

    print("\nProbando con objetivo que no está en la lista:")
    objetivo_no_e_ej2 = 100
    print(f"Lista: {lista_ej2}, Objetivo: {objetivo_no_e_ej2}")
    indice_no_e_ej2 = busqueda_lineal_contando(lista_ej2, objetivo_no_e_ej2)
    if indice_no_e_ej2 != -1:
        print(f"El objetivo {objetivo_no_e_ej2} se encontró en el índice: {indice_no_e_ej2}")
    else:
        print(f"El objetivo {objetivo_no_e_ej2} no se encontró en la lista.")

def test_ejercicio_3():
    print("\n--- Ejecutando Ejercicio 3: Búsqueda Binaria ---")
    lista_ej3 = [1, 3, 5, 7, 9, 11, 13, 15] 
    objetivo_ej3 = 7
    print(f"Lista (ordenada): {lista_ej3}, Objetivo: {objetivo_ej3}")
    indice = busqueda_binaria(lista_ej3, objetivo_ej3)
    if indice != -1:
        print(f"El objetivo {objetivo_ej3} se encontró en el índice: {indice}")
    else:
        print(f"El objetivo {objetivo_ej3} no se encontró en la lista.")

    objetivo_no_encontrado_ej3 = 10
    print(f"\nLista (ordenada): {lista_ej3}, Objetivo: {objetivo_no_encontrado_ej3}")
    indice_no_e_ej3 = busqueda_binaria(lista_ej3, objetivo_no_encontrado_ej3)
    if indice_no_e_ej3 != -1:
        print(f"El objetivo {objetivo_no_encontrado_ej3} se encontró en el índice: {indice_no_e_ej3}")
    else:
        print(f"El objetivo {objetivo_no_encontrado_ej3} no se encontró en la lista.")

def test_ejercicio_4():
    print("\n--- Ejecutando Ejercicio 4: Búsqueda Binaria Contando Pasos ---")
    lista_ej4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
    objetivo_ej4 = 11
    print(f"Lista (ordenada): {lista_ej4}, Objetivo: {objetivo_ej4}")
    indice = busqueda_binaria_contando(lista_ej4, objetivo_ej4)
    if indice != -1:
        print(f"El objetivo {objetivo_ej4} se encontró en el índice: {indice}")
    else:
        print(f"El objetivo {objetivo_ej4} no se encontró en la lista.")

    print("\nProbando con objetivo que no está en la lista:")
    objetivo_no_e_ej4 = 2
    print(f"Lista (ordenada): {lista_ej4}, Objetivo: {objetivo_no_e_ej4}")
    indice_no_e_ej4 = busqueda_binaria_contando(lista_ej4, objetivo_no_e_ej4)
    if indice_no_e_ej4 != -1:
        print(f"El objetivo {objetivo_no_e_ej4} se encontró en el índice: {indice_no_e_ej4}")
    else:
        print(f"El objetivo {objetivo_no_e_ej4} no se encontró en la lista.")

def test_ejercicio_7():
    print("\n--- Ejecutando Ejercicio 7: Contar Ocurrencias ---")
    lista_ej7 = [1, 5, 2, 5, 3, 5, 4, 5]
    numero_a_contar = 5
    print(f"Lista: {lista_ej7}, Número a contar: {numero_a_contar}")
    ocurrencias = contar_ocurrencias(lista_ej7, numero_a_contar)
    print(f"El número {numero_a_contar} aparece {ocurrencias} veces.")

    numero_no_presente = 10
    print(f"\nLista: {lista_ej7}, Número a contar: {numero_no_presente}")
    ocurrencias_no_presente = contar_ocurrencias(lista_ej7, numero_no_presente)
    print(f"El número {numero_no_presente} aparece {ocurrencias_no_presente} veces.")

def test_ejercicio_9():
    print("\n--- Ejecutando Ejercicio 9: Búsqueda en Diccionario por Valor ---")
    personas_ej9 = {"Alice": 25, "Bob": 30, "Charlie": 22, "David": 30}
    edad_a_buscar_1 = 30
    print(f"Diccionario: {personas_ej9}, Edad a buscar: {edad_a_buscar_1}")
    nombre_encontrado_1 = buscar_por_edad(personas_ej9, edad_a_buscar_1)
    print(f"Nombre asociado a la edad {edad_a_buscar_1}: {nombre_encontrado_1}")
    

    edad_a_buscar_2 = 22
    print(f"\nDiccionario: {personas_ej9}, Edad a buscar: {edad_a_buscar_2}")
    nombre_encontrado_2 = buscar_por_edad(personas_ej9, edad_a_buscar_2)
    print(f"Nombre asociado a la edad {edad_a_buscar_2}: {nombre_encontrado_2}")

    edad_no_encontrada = 40
    print(f"\nDiccionario: {personas_ej9}, Edad a buscar: {edad_no_encontrada}")
    nombre_no_e = buscar_por_edad(personas_ej9, edad_no_encontrada)
    print(f"Nombre asociado a la edad {edad_no_encontrada}: {nombre_no_e}")


# --- FUNCIÓN PRINCIPAL DEL MENÚ ---

def main():
    """
    Función principal que muestra un menú interactivo para seleccionar
    y ejecutar cada ejercicio.
    """

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
        print("\n" + "="*40)
        print("         Menú de Ejercicios del TP")
        print("="*40)
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
        print("="*40)

        choice = input("Seleccione el ejercicio a ejecutar (1-9) o 'q' para salir: ").strip().lower()

        if choice == 'q':
            print("\nSaliendo del programa. ¡Adiós!")
            break
        elif choice in exercises:
            # Llama a la función asociada directamente desde el diccionario
            exercises[choice]()
            print("\n--- Fin del Ejercicio ---")
        else:
            print("\n¡ERROR! Elección inválida. Por favor, ingrese un número del 1 al 9 o 'q'.")
            time.sleep(1) # Pequeña pausa para que el usuario lea el error

if __name__ == "__main__":
    main()