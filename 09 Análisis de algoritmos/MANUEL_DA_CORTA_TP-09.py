import time
import random # Utilizado para generar datos en pruebas empíricas

# --- Información del Trabajo Práctico ---
# Universidad Tecnológica Nacional (UTN) - Tecnicatura Universitaria en Programación a Distancia
# Asignatura: Programación I
# Trabajo Práctico: Análisis de Algoritmos
# Alumno: [Tu Nombre Completo Aquí]
# Fecha: 21 de Mayo de 2025

print("Estimado profesor/a, presento a continuación mi Trabajo Práctico sobre Análisis de Algoritmos.")
print("El objetivo es determinar la complejidad temporal de diversos algoritmos utilizando la notación Big-O,")
print("así como comparar la eficiencia de distintas soluciones y observar su comportamiento empírico.")
print("-" * 70)

# --- Implementaciones de los Algoritmos (para las pruebas empíricas) ---

def suma_numeros_ej1(n):
    """Calcula la suma de los primeros n números de forma iterativa."""
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def suma_numeros_formula_ej2(n):
    """Calcula la suma de los primeros n números utilizando la fórmula de Gauss."""
    return (n * (n + 1)) // 2

def buscar_elemento_ej3(lista, objetivo):
    """Busca un elemento en una lista desordenada."""
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

def encontrar_maximo_ej4(lista):
    """Encuentra el número máximo en una lista."""
    # Se asume que la lista no está vacía, según el contexto del ejercicio.
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo

def ordenamiento_seleccion_ej5(lista):
    """Implementación del algoritmo de Ordenamiento por Selección."""
    n = len(lista)
    for i in range(n):
        min_idx = i
        # Bucle interno para encontrar el índice del elemento mínimo en la sublista no ordenada
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambio del elemento mínimo encontrado con el primer elemento de la sublista no ordenada
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# --- Funciones para el Análisis y Presentación del Menú ---

def analizar_ejercicio_1():
    """Presenta el análisis del Ejercicio 1: Suma iterativa."""
    print("\n" + "=" * 70)
    print(" EJERCICIO 1: Suma de los primeros n números (Enfoque Iterativo) ")
    print("=" * 70)

    print("\nEl código analizado es el siguiente:")
    print("""
def suma_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma
""")
    print("\nAnálisis de la Complejidad Temporal (T(n) y O(n)):")
    print("1. `suma = 0`: Operación de asignación inicial. Costo constante, O(1).")
    print("2. `for i in range(1, n+1)`: Este bucle se ejecuta 'n' veces.")
    print("3. `suma += i`: Operación de suma y asignación. Se realiza en cada iteración del bucle, por lo tanto, 'n' veces. Cada operación tiene un costo constante.")
    print("4. `return suma`: Operación de retorno. Costo constante, O(1).")
    print("\nJustificación de la Complejidad:")
    print("La cantidad de operaciones que realiza el algoritmo es directamente proporcional al valor de 'n'.")
    print("El bucle for es el factor dominante, ya que se ejecuta 'n' veces y las operaciones internas son constantes.")
    print("\nDeterminación de la Complejidad:")
    print(f"La función de complejidad temporal T(n) se puede expresar como: T(n) = C1 + C2 * n + C3")
    print(f"Por lo tanto, en notación Big-O, su orden de complejidad es: O(n) (Lineal)")

    # Prueba empírica para ilustrar el comportamiento
    print(f"\n--- Prueba Empírica (con n = 1.000.000) ---")
    n_prueba = 1_000_000
    start_time = time.time()
    resultado_ej1 = suma_numeros_ej1(n_prueba)
    end_time = time.time()
    print(f"Resultado de suma_numeros({n_prueba}): {resultado_ej1}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")

def analizar_ejercicio_2():
    """Presenta el análisis del Ejercicio 2: Suma con fórmula y comparación."""
    print("\n" + "=" * 70)
    print(" EJERCICIO 2: Suma de los primeros n números (Enfoque con Fórmula Gaussiana) ")
    print("=" * 70)

    print("\nEl código analizado es el siguiente:")
    print("""
def suma_numeros_formula(n):
    return (n * (n + 1)) // 2
""")
    print("\nAnálisis de la Complejidad Temporal (T(n) y O(n)):")
    print("1. `return (n * (n + 1)) // 2`: Esta línea contiene un número fijo de operaciones aritméticas (una multiplicación, una suma, una división entera).")
    print("2. Estas operaciones se realizan en un número constante de pasos, independientemente del valor de 'n'.")
    print("\nJustificación de la Complejidad:")
    print("El número de operaciones en esta función no depende del valor de 'n'. No hay bucles ni recursión que escalen con el tamaño de la entrada.")
    print("\nDeterminación de la Complejidad:")
    print(f"La función de complejidad temporal T(n) es una constante: T(n) = C")
    print(f"Por lo tanto, en notación Big-O, su orden de complejidad es: O(1) (Constante)")

    # Prueba empírica para ilustrar el comportamiento
    n_prueba = 1_000_000_000 # Un valor grande para n
    print(f"\n--- Prueba Empírica (con n = {n_prueba:,}) ---")
    start_time = time.time()
    resultado_ej2 = suma_numeros_formula_ej2(n_prueba)
    end_time = time.time()
    print(f"Resultado de suma_numeros_formula({n_prueba}): {resultado_ej2}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")

    print("\n" + "=" * 70)
    print(" Comparación de Eficiencia: Ejercicio 1 (O(n)) vs. Ejercicio 2 (O(1)) ")
    print("=" * 70)
    print("El análisis demuestra que la solución del Ejercicio 1 (O(n)) tiene una complejidad lineal, mientras que la del Ejercicio 2 (O(1)) es constante.")
    print("A medida que el valor de 'n' aumenta, el tiempo de ejecución del Ejercicio 1 crece linealmente,")
    print("mientras que el tiempo de ejecución del Ejercicio 2 permanece prácticamente inalterado.")
    print("En consecuencia, la solución del **Ejercicio 2 es considerablemente más eficiente**, especialmente para grandes volúmenes de datos.")

def analizar_ejercicio_3():
    """Presenta el análisis del Ejercicio 3: Búsqueda lineal."""
    print("\n" + "=" * 70)
    print(" EJERCICIO 3: Búsqueda de un elemento en una lista desordenada ")
    print("=" * 70)

    print("\nEl código analizado es el siguiente:")
    print("""
def buscar_elemento(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False
""")
    print("\nAnálisis de la Complejidad Temporal (Peor Caso) (T(n) y O(n)):")
    print("Sea 'n' la cantidad de elementos en la 'lista'.")
    print("1. `for elemento in lista:`: Este bucle itera sobre cada elemento de la lista.")
    print("2. `if elemento == objetivo:`: La operación de comparación se realiza en cada iteración del bucle.")
    print("3. `return True`/`return False`: Operaciones de retorno, constantes.")
    print("\nDeterminación del Peor Caso:")
    print("El peor caso para este algoritmo se presenta en dos escenarios:")
    print("  a) El `objetivo` no se encuentra en la lista: el algoritmo debe recorrer la lista completa.")
    print("  b) El `objetivo` es el último elemento de la lista: el algoritmo también debe recorrer la lista hasta el final.")
    print("\nJustificación de la Complejidad (Peor Caso):")
    print("En el peor de los casos, el algoritmo ejecuta un número de operaciones directamente proporcional a la longitud de la lista ('n').")
    print("El bucle realiza 'n' iteraciones, y las operaciones dentro de cada iteración son de tiempo constante.")
    print("\nResultado:")
    print(f"Su complejidad temporal en el peor caso es: O(n) (Lineal)")

    # Prueba empírica (peor caso)
    n_prueba = 100_000
    lista_grande_peor_caso = list(range(n_prueba))
    objetivo_no_existe = n_prueba + 1 # Este elemento no está en la lista
    print(f"\n--- Prueba Empírica (Lista de {n_prueba:,} elementos, Peor Caso) ---")
    start_time = time.time()
    encontrado = buscar_elemento_ej3(lista_grande_peor_caso, objetivo_no_existe)
    end_time = time.time()
    print(f"¿Elemento {objetivo_no_existe} encontrado?: {encontrado}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")

    # Prueba empírica (mejor caso)
    objetivo_existe_al_principio = 0
    print(f"\n--- Prueba Empírica (Lista de {n_prueba:,} elementos, Mejor Caso) ---")
    start_time = time.time()
    encontrado_mejor = buscar_elemento_ej3(lista_grande_peor_caso, objetivo_existe_al_principio)
    end_time = time.time()
    print(f"¿Elemento {objetivo_existe_al_principio} encontrado?: {encontrado_mejor}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")


def analizar_ejercicio_4():
    """Presenta el análisis del Ejercicio 4: Encontrar el máximo."""
    print("\n" + "=" * 70)
    print(" EJERCICIO 4: Encontrar el número máximo en una lista ")
    print("=" * 70)

    print("\nEl código analizado es el siguiente:")
    print("""
def encontrar_maximo(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo
""")
    print("\nAnálisis de la Complejidad Temporal (T(n) y O(n)):")
    print("Sea 'n' la cantidad de elementos en la 'lista'.")
    print("1. `maximo = lista[0]`: Operación de asignación e indexación. Costo constante, O(1).")
    print("2. `for elemento in lista:`: Este bucle itera sobre todos los 'n' elementos de la lista.")
    print("3. `if elemento > maximo:`: Esta comparación se realiza en cada una de las 'n' iteraciones del bucle. Costo constante por comparación.")
    print("4. `maximo = elemento`: Esta asignación se realiza solo cuando se encuentra un nuevo máximo. Aunque su frecuencia varía, la comparación siempre se ejecuta.")
    print("5. `return maximo`: Operación de retorno. Costo constante, O(1).")
    print("\nJustificación de la Complejidad:")
    print("El algoritmo debe recorrer indefectiblemente todos los elementos de la lista para garantizar que ha encontrado el valor máximo.")
    print("Por lo tanto, la cantidad total de operaciones es directamente proporcional al tamaño de la lista.")
    print("\nResultado:")
    print(f"Su complejidad temporal es: O(n) (Lineal)")

    # Prueba empírica
    n_prueba = 500_000
    lista_grande_aleatoria = [random.randint(0, 1_000_000) for _ in range(n_prueba)]
    print(f"\n--- Prueba Empírica (Lista de {n_prueba:,} elementos) ---")
    start_time = time.time()
    max_val = encontrar_maximo_ej4(lista_grande_aleatoria)
    end_time = time.time()
    print(f"El valor máximo encontrado: {max_val}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos.")


def analizar_ejercicio_5():
    """Presenta el análisis del Ejercicio 5: Ordenamiento por Selección."""
    print("\n" + "=" * 70)
    print(" EJERCICIO 5: Ordenamiento por Selección ")
    print("=" * 70)

    print("\nEl código analizado es el siguiente:")
    print("""
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
""")
    print("\nAnálisis de la Complejidad Temporal (T(n) y O(n)):")
    print("Sea 'n' la cantidad de elementos en la 'lista'.")
    print("1. `n = len(lista)`: Operación de tiempo constante, O(1).")
    print("2. **Bucle exterior** `for i in range(n)`: Este bucle se ejecuta 'n' veces.")
    print("3. `min_idx = i`: Asignación de tiempo constante dentro del bucle exterior.")
    print("4. **Bucle interior anidado** `for j in range(i + 1, n)`:")
    print("   - Este bucle es el principal contribuyente a la complejidad.")
    print("   - Para `i=0`, se ejecuta `n-1` veces.")
    print("   - Para `i=1`, se ejecuta `n-2` veces.")
    print("   - ... y así sucesivamente, hasta que para `i=n-2`, se ejecuta 1 vez.")
    print("   - La suma total de iteraciones de este bucle interior es aproximadamente $n*(n-1)/2$, lo que es un término cuadrático ($O(n^2)$).")
    print("5. `if lista[j] < lista[min_idx]`: La operación de comparación dentro del bucle interior se ejecuta $O(n^2)$ veces en total.")
    print("6. `min_idx = j`: La asignación se realiza cuando se encuentra un nuevo mínimo, lo que puede ocurrir hasta $O(n^2)$ veces.")
    print("7. `lista[i], lista[min_idx] = ...`: La operación de intercambio de elementos se realiza una vez por cada iteración del bucle exterior (`n` veces). Consiste en un número fijo de asignaciones, por lo tanto, es $O(1)$.")

    print("\nComportamiento en el Peor Caso:")
    print("Una característica notable del Ordenamiento por Selección es que su complejidad temporal en el peor caso es la misma que en el mejor caso y el caso promedio.")
    print("Esto se debe a que el algoritmo siempre realiza la misma cantidad de comparaciones para encontrar el elemento mínimo en cada sublista no ordenada y, luego, realiza el intercambio.")
    print("El orden inicial de los elementos de la lista no afecta significativamente el número total de operaciones de comparación, que es el factor dominante.")
    print("\nDeterminación de la Complejidad:")
    print(f"El factor dominante es el doble bucle anidado. La cantidad de operaciones crece cuadráticamente con el tamaño de la lista.")
    print(f"Su complejidad temporal es: O(n^2) (Cuadrática)")

    # Prueba empírica
    n_prueba_corta = 5000 # Un valor moderado para n, ya que O(n^2) escala rápidamente
    lista_prueba_aleatoria = [random.randint(0, 100000) for _ in range(n_prueba_corta)]
    print(f"\n--- Prueba Empírica (Lista de {n_prueba_corta:,} elementos) ---")
    lista_copia = lista_prueba_aleatoria[:] # Crear una copia para no modificar la lista original
    start_time = time.time()
    ordenamiento_seleccion_ej5(lista_copia) # No imprimimos la lista ordenada para ahorrar espacio
    end_time = time.time()
    print(f"Tiempo de ejecución para ordenar {n_prueba_corta:,} elementos: {end_time - start_time:.6f} segundos.")
    print(f"Se observa que para N=5000, un algoritmo O(N^2) ya toma un tiempo considerable.")


# --- Menú principal de interacción ---

def mostrar_menu():
    print("\n" + "*" * 70)
    print(" MENÚ DE EJERCICIOS DE ANÁLISIS DE ALGORITMOS ".center(70))
    print("*" * 70)
    print("1. Ejercicio 1: Suma de Números (Iterativa - O(n))")
    print("2. Ejercicio 2: Suma de Números (Fórmula - O(1) y Comparación)")
    print("3. Ejercicio 3: Búsqueda Lineal (O(n) en el peor caso)")
    print("4. Ejercicio 4: Encontrar el Máximo (O(n))")
    print("5. Ejercicio 5: Ordenamiento por Selección (O(n^2))")
    print("0. Salir del Programa")
    print("-" * 70)

def main():
    while True:
        mostrar_menu()
        opcion = input("Por favor, ingrese el número del ejercicio a analizar (o '0' para salir): ")

        if opcion == '1':
            analizar_ejercicio_1()
        elif opcion == '2':
            analizar_ejercicio_2()
        elif opcion == '3':
            analizar_ejercicio_3()
        elif opcion == '4':
            analizar_ejercicio_4()
        elif opcion == '5':
            analizar_ejercicio_5()
        elif opcion == '0':
            print("\nGracias por su tiempo. Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, intente con un número entre 0 y 5.")

        input("\nPresione ENTER para volver al menú principal...") # Pausa la ejecución hasta que el usuario presione Enter

if __name__ == "__main__":
    main()