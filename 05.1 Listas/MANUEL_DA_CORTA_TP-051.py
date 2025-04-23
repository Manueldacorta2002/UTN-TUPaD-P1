def mostrar_menu():
    print("\n=== MENÚ TP 5 - LISTAS ===")
    print("1. Múltiplos de 4 del 1 al 100")
    print("2. Mostrar penúltimo elemento de lista")
    print("3. Lista vacía con append")
    print("4. Reemplazar elementos en lista 'animales'")
    print("5. Analizar programa con remove(max())")
    print("6. Números del 10 al 30 con saltos de 5")
    print("7. Reemplazar valores centrales en 'autos'")
    print("8. Lista 'dobles' con append")
    print("9. Manipulación de lista anidada 'compras'")
    print("10. Crear lista anidada específica")
    print("0. Salir")
    return input("Seleccione un ejercicio (1-10) o 0 para salir: ")

def ejercicio_1():
    print("\nEjercicio 1: Múltiplos de 4 del 1 al 100")
    multiplos_de_4 = list(range(4, 101, 4))
    print(f"Lista resultante: {multiplos_de_4}")
    print(f"Cantidad de elementos: {len(multiplos_de_4)}")

def ejercicio_2():
    print("\nEjercicio 2: Mostrar penúltimo elemento")
    mi_lista = ["pizza", "helado", "chocolate", "viajes", "música"]
    print(f"Lista original: {mi_lista}")
    print(f"Penúltimo elemento: {mi_lista[-2]}")  

def ejercicio_3():
    print("\nEjercicio 3: Lista vacía con append")
    lista_vacia = []
    lista_vacia.append("Python")
    lista_vacia.append("Programación")
    lista_vacia.append("Listas")
    print(f"Lista resultante: {lista_vacia}")

def ejercicio_4():
    print("\nEjercicio 4: Reemplazar en lista 'animales'")
    animales = ["perro", "gato", "conejo", "pez"]
    print(f"Lista original: {animales}")
    animales[1] = "loro"   
    animales[-1] = "oso"    
    print(f"Lista modificada: {animales}")

def ejercicio_5():
    print("\nEjercicio 5: Análisis de programa")
    numeros = [8, 15, 3, 22, 7]
    print(f"Lista original: {numeros}")
    print("max(numeros) devuelve el valor máximo (22)")
    print("remove() elimina la primera ocurrencia de ese valor")
    numeros.remove(max(numeros))
    print(f"Lista resultante: {numeros}")
    print("El programa elimina el número más grande de la lista")

def ejercicio_6():
    print("\nEjercicio 6: Números del 10 al 30 con saltos de 5")
    numeros = list(range(10, 31, 5))
    print(f"Lista completa: {numeros}")
    print(f"Los dos primeros elementos: {numeros[:2]}")

def ejercicio_7():
    print("\nEjercicio 7: Reemplazar valores centrales en 'autos'")
    autos = ["sedan", "polo", "suran", "gol"]
    print(f"Lista original: {autos}")
    autos[1:3] = ["ford", "chevrolet"]  
    print(f"Lista modificada: {autos}")

def ejercicio_8():
    print("\nEjercicio 8: Lista 'dobles' con append")
    dobles = []
    dobles.append(5 * 2)
    dobles.append(10 * 2)
    dobles.append(15 * 2)
    print(f"Lista resultante: {dobles}")

def ejercicio_9():
    print("\nEjercicio 9: Manipulación de lista anidada 'compras'")
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    print(f"Lista original: {compras}")
    
    # a) Agregar "jugo" al tercer cliente
    compras[2].append("jugo")
    
    # b) Reemplazar "fideos" por "tallarines"
    compras[1][1] = "tallarines"
    
    # c) Eliminar "pan" del primer cliente
    compras[0].remove("pan")
    
    print(f"Lista modificada: {compras}")

def ejercicio_10():
    print("\nEjercicio 10: Crear lista anidada específica")
    lista_anidada = [
        15,
        True,
        [25.5, 57.9, 30.6],
        False
    ]
    print(f"Lista creada: {lista_anidada}")
    print(f"lista_anidada[2][1] = {lista_anidada[2][1]}")  

# Programa principal con switch
def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            ejercicio_9()
        elif opcion == "10":
            ejercicio_10()
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()