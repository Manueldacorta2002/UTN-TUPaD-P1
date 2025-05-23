

class Nodo:
    """
    Clase Nodo para representar un nodo en un árbol o grafo.
    Utilizada en los ejercicios 1 y 2.
    """
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []  # Para nodos hijos en una estructura de árbol
        self.padre = None  # Para el nodo padre en una estructura de árbol

    def buscar_camino(self, destino_valor, camino_actual=None):
        """
        Busca un camino desde el nodo actual hasta un nodo con 'destino_valor'.
        Retorna una lista de valores de nodos que forman el camino, o None si no se encuentra.
        """
        if camino_actual is None:
            camino_actual = []
        camino_actual = camino_actual + [self.valor]

        if self.valor == destino_valor:
            return camino_actual

        # Asumimos una búsqueda en profundidad para una estructura tipo árbol simple
        for hijo in self.hijos:
            camino = hijo.buscar_camino(destino_valor, camino_actual)
            if camino:
                return camino
        return None

    def calcular_longitud_de_camino(self, camino):
        """
        Calcula la longitud de un camino (número de aristas).
        Retorna None si el camino es None. [cite: 5, 6]
        """
        if camino is None:
            return None
        # La longitud del camino es el número de aristas, que es el número de nodos - 1
        return len(camino) - 1

    def obtener_hijos(self):
        """
        Imprime por pantalla si el nodo tiene hijos y, en caso de tener, cuáles nodos son. [cite: 7]
        """
        if self.hijos:
            print(f"El nodo '{self.valor}' tiene hijos: {[hijo.valor for hijo in self.hijos]}")
        else:
            print(f"El nodo '{self.valor}' no tiene hijos.")

    def obtener_padre(self):
        """
        Imprime por pantalla si el nodo tiene padre y, en caso de tener, cuál nodo es. [cite: 8]
        """
        if self.padre:
            print(f"El nodo '{self.valor}' tiene como padre a: {self.padre.valor}")
        else:
            print(f"El nodo '{self.valor}' no tiene padre.")

    def obtener_tipo(self):
        """
        Imprime por pantalla si el nodo es raíz, rama u hoja. [cite: 1]
        """
        if self.padre is None and not self.hijos:
            print(f"El nodo '{self.valor}' es un nodo aislado (o es raíz y hoja a la vez si el árbol tiene solo un nodo).")
        elif self.padre is None:
            print(f"El nodo '{self.valor}' es la raíz.")
        elif not self.hijos:
            print(f"El nodo '{self.valor}' es una hoja.")
        else:
            print(f"El nodo '{self.valor}' es una rama.")


class NodoArbol:
    """
    Clase Nodo para ser usada específicamente en ArbolBusquedaBinario.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBusquedaBinario:
    """
    Clase para un Árbol Binario de Búsqueda.
    Utilizada en el ejercicio 3.
    """
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un nuevo valor en el árbol binario de búsqueda."""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)
        # Si el valor ya existe, no se hace nada

    def buscar_nodo(self, valor_a_buscar):
        """
        Busca un nodo con el valor dado en el árbol binario.
        Retorna True si lo contiene, False en caso contrario. [cite: 10]
        """
        return self._buscar_nodo_recursivo(self.raiz, valor_a_buscar)

    def _buscar_nodo_recursivo(self, nodo_actual, valor_a_buscar):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor_a_buscar:
            return True
        elif valor_a_buscar < nodo_actual.valor:
            return self._buscar_nodo_recursivo(nodo_actual.izquierda, valor_a_buscar)
        else:
            return self._buscar_nodo_recursivo(nodo_actual.derecha, valor_a_buscar)



def crear_listas_adyacencia_dirigida(nodos, aristas):
    """
    Crea y retorna las listas de adyacencia para un grafo dirigido. [cite: 11]
    nodos: una lista de los valores de los nodos (ej. ['A', 'B', 'C'])
    aristas: una lista de tuplas (origen, destino) representando las aristas (ej. [('A', 'B')]) [cite: 13, 14]
    """
    adj_list = {nodo: [] for nodo in nodos}
    for origen, destino in aristas:
        if origen in adj_list and destino in adj_list:
            adj_list[origen].append(destino)
        else:
            print(f"Advertencia: La arista ('{origen}', '{destino}') contiene nodos no definidos en la lista de nodos.")
    return adj_list

def crear_matriz_adyacencia_dirigida(nodos, aristas):
    """
    Crea y retorna la matriz de adyacencia para un grafo dirigido. [cite: 12]
    nodos: una lista de los valores de los nodos (ej. ['A', 'B', 'C'])
    aristas: una lista de tuplas (origen, destino) representando las aristas (ej. [('A', 'B')]) [cite: 13, 14]
    """
    num_nodos = len(nodos)
    # Crear un mapeo de nodo a índice para la matriz
    nodo_a_indice = {nodo: i for i, nodo in enumerate(nodos)}

    # Inicializar la matriz con ceros
    matriz_adyacencia = [[0 for _ in range(num_nodos)] for _ in range(num_nodos)]

    for origen, destino in aristas:
        if origen in nodo_a_indice and destino in nodo_a_indice:
            idx_origen = nodo_a_indice[origen]
            idx_destino = nodo_a_indice[destino]
            matriz_adyacencia[idx_origen][idx_destino] = 1
        else:
            print(f"Advertencia: La arista ('{origen}', '{destino}') contiene nodos no definidos en la lista de nodos.")
    return matriz_adyacencia, nodos # Retornamos también los nodos para referencia del orden

# --- FUNCIÓN PRINCIPAL DEL MENÚ ---

def ejecutar_ejercicio(opcion):
    """
    Ejecuta el ejercicio seleccionado por el usuario.
    """
    if opcion == '1':
        print("\n--- Ejecutando Ejercicio 1: Clase Nodo con calcular_longitud_de_camino ---")

        nodo_a = Nodo("A")
        nodo_b = Nodo("B")
        nodo_c = Nodo("C")
        nodo_d = Nodo("D")
        nodo_e = Nodo("E")

        nodo_a.hijos.append(nodo_b)
        nodo_a.hijos.append(nodo_c)
        nodo_b.padre = nodo_a
        nodo_c.padre = nodo_a

        nodo_c.hijos.append(nodo_d)
        nodo_c.hijos.append(nodo_e)
        nodo_d.padre = nodo_c
        nodo_e.padre = nodo_c

        print("\nProbando buscar_camino y calcular_longitud_de_camino:")
        camino_a_e = nodo_a.buscar_camino("E")
        print(f"Camino de A a E: {camino_a_e}")
        print(f"Longitud del camino de A a E: {nodo_a.calcular_longitud_de_camino(camino_a_e)}")

        camino_a_f = nodo_a.buscar_camino("F") 
        print(f"Camino de A a F: {camino_a_f}")
        print(f"Longitud del camino de A a F (debería ser None): {nodo_a.calcular_longitud_de_camino(camino_a_f)}")

    elif opcion == '2':
        print("\n--- Ejecutando Ejercicio 2: Modificar Clase Nodo con obtener_hijos, obtener_padre, obtener_tipo ---")
       
        nodo_a = Nodo("A")
        nodo_b = Nodo("B")
        nodo_c = Nodo("C")
        nodo_d = Nodo("D")
        nodo_e = Nodo("E")

        nodo_a.hijos.append(nodo_b)
        nodo_a.hijos.append(nodo_c)
        nodo_b.padre = nodo_a
        nodo_c.padre = nodo_a

        nodo_c.hijos.append(nodo_d)
        nodo_c.hijos.append(nodo_e)
        nodo_d.padre = nodo_c
        nodo_e.padre = nodo_c

        print("\nProbando obtener_tipo:")
        nodo_a.obtener_tipo()
        nodo_b.obtener_tipo()
        nodo_c.obtener_tipo()
        nodo_d.obtener_tipo()

        print("\nProbando obtener_hijos:")
        nodo_a.obtener_hijos()
        nodo_c.obtener_hijos()
        nodo_b.obtener_hijos()
        
        print("\nProbando obtener_padre:")
        nodo_a.obtener_padre()
        nodo_b.obtener_padre()
        nodo_d.obtener_padre()

    elif opcion == '3':
        print("\n--- Ejecutando Ejercicio 3: Clase ArbolBusquedaBinario con buscar_nodo ---")
        abb = ArbolBusquedaBinario()
        print("Insertando valores: 50, 30, 70, 20, 40, 60, 80")
        abb.insertar(50)
        abb.insertar(30)
        abb.insertar(70)
        abb.insertar(20)
        abb.insertar(40)
        abb.insertar(60)
        abb.insertar(80)

        print(f"\n¿El árbol contiene el valor 40? {abb.buscar_nodo(40)}")
        print(f"¿El árbol contiene el valor 90? {abb.buscar_nodo(90)}")
        print(f"¿El árbol contiene el valor 50? {abb.buscar_nodo(50)}")
        print(f"¿El árbol contiene el valor 25? {abb.buscar_nodo(25)}")

    elif opcion == '4':
        print("\n--- Ejecutando Ejercicio 4: Funciones para adyacencia de grafos dirigidos ---")
        
        # La prueba se hace en el Ejercicio 5.
        print("Las funciones 'crear_listas_adyacencia_dirigida' y 'crear_matriz_adyacencia_dirigida' han sido definidas.")
        print("Puedes probarlas con el Ejercicio 5.")

    elif opcion == '5':
        print("\n--- Ejecutando Ejercicio 5: Probar funciones de grafo con grafo dado ---")
        nodos_grafo = ['A', 'B', 'C']
        aristas_grafo = [('A', 'B'), ('A', 'C')]

        print("\n--- Probando crear_listas_adyacencia_dirigida ---")
        listas_adyacencia = crear_listas_adyacencia_dirigida(nodos_grafo, aristas_grafo)
        print("Listas de Adyacencia:")
        for nodo, adyacentes in listas_adyacencia.items():
            print(f"{nodo}: {adyacentes}")

        print("\n--- Probando crear_matriz_adyacencia_dirigida ---")
        matriz_adyacencia, orden_nodos = crear_matriz_adyacencia_dirigida(nodos_grafo, aristas_grafo)
        print("Matriz de Adyacencia (orden de nodos: " + str(orden_nodos) + "):")
        for fila in matriz_adyacencia:
            print(fila)

    else:
        print("Opción no válida. Por favor, ingrese un número entre 1 y 5.")

# --- MENÚ PRINCIPAL ---
def main():
    while True:
        print("\n--- Menú de Ejercicios del TP 12 ---")
        print("1. Ejercicio 1: Clase Nodo con calcular_longitud_de_camino")
        print("2. Ejercicio 2: Modificar Clase Nodo con obtener_hijos, obtener_padre, obtener_tipo")
        print("3. Ejercicio 3: Clase ArbolBusquedaBinario con buscar_nodo")
        print("4. Ejercicio 4: Funciones para adyacencia de grafos dirigidos (Creación de funciones)")
        print("5. Ejercicio 5: Probar funciones de grafo con grafo dado")
        print("0. Salir")

        opcion = input("Seleccione un ejercicio para ejecutar (0-5): ")

        if opcion == '0':
            print("Saliendo del programa.")
            break
        
        ejecutar_ejercicio(opcion)

if __name__ == "__main__":
    main()