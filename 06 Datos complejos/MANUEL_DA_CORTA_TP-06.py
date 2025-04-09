import math
from collections import deque

# Ejercicio 1 y 2
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

def ejercicio1():
    precios_frutas.update({
        'Naranja': 1200,
        'Manzana': 1500,
        'Pera': 2300
    })
    print("Frutas agregadas:", precios_frutas)

def ejercicio2():
    precios_frutas.update({
        'Banana': 1330,
        'Manzana': 1700,
        'Melón': 2800
    })
    print("Precios actualizados:", precios_frutas)

def ejercicio3():
    frutas = list(precios_frutas.keys())
    print("Lista de frutas:", frutas)

# Ejercicio 4
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

def ejercicio4():
    persona = Persona("Manuel", "Argentina", 22)
    persona.saludar()

# Ejercicio 5
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

def ejercicio5():
    circulo = Circulo(5)
    print("Área:", circulo.calcular_area())
    print("Perímetro:", circulo.calcular_perimetro())

# Ejercicio 6
def ejercicio6():
    def balanceado(cadena):
        pila = []
        pares = {')': '(', '}': '{', ']': '['}
        for caracter in cadena:
            if caracter in '([{':
                pila.append(caracter)
            elif caracter in ')]}':
                if not pila or pila[-1] != pares[caracter]:
                    return False
                pila.pop()
        return not pila

    cadena = input("Ingresá una cadena con paréntesis: ")
    print("¿Está balanceada?", balanceado(cadena))

# Ejercicio 7
cola = deque()

def ejercicio7():
    while True:
        print("\n1. Agregar cliente\n2. Atender cliente\n3. Ver siguiente\n4. Salir")
        opcion = input("Elegí una opción: ")
        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            cola.append(cliente)
        elif opcion == "2":
            if cola:
                print("Atendiendo a:", cola.popleft())
            else:
                print("No hay clientes en espera.")
        elif opcion == "3":
            if cola:
                print("Siguiente cliente:", cola[0])
            else:
                print("No hay clientes.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

# Ejercicio 8 y 9 - Lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

lista = ListaEnlazada()

def ejercicio8():
    lista.insertar_inicio(10)
    lista.insertar_inicio(20)
    lista.insertar_inicio(30)
    print("Lista enlazada:")
    lista.mostrar()

def ejercicio9():
    print("Lista antes de invertir:")
    lista.mostrar()
    lista.invertir()
    print("Lista invertida:")
    lista.mostrar()

# Menú principal 
def menu():
    while True:
        print("""
-------- MENÚ --------
1. Añadir frutas al diccionario
2. Actualizar precios de frutas
3. Mostrar solo nombres de frutas
4. Crear y saludar con una persona
5. Calcular área y perímetro de un círculo
6. Verificar paréntesis balanceados
7. Simular cola en banco
8. Insertar nodos en lista enlazada
9. Invertir lista enlazada
0. Salir
""")
        try:
            opcion = int(input("Elegí una opción: "))
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
                case 0: break
                case _: print("Opción inválida")
        except ValueError:
            print("Por favor ingresá un número.")

menu()
