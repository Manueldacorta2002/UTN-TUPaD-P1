"""
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
TRABAJO PRÁCTICO 3 - ESTRUCTURAS CONDICIONALES
Alumno: Manuel Da Cortá

Este programa implementa un menú interactivo que permite seleccionar y ejecutar
cada uno de los ejercicios del TP3 sobre estructuras condicionales.
"""

def mostrar_menu():
    """Muestra el menú de opciones con los ejercicios disponibles"""
    print("\n" + "="*50)
    print("TP 3 - ESTRUCTURAS CONDICIONALES - MENÚ PRINCIPAL")
    print("="*50)
    print("1. Ejercicio 1 - Mayor de edad")
    print("2. Ejercicio 2 - Aprobado/Desaprobado")
    print("3. Ejercicio 3 - Números pares")
    print("4. Ejercicio 4 - Categorías por edad")
    print("5. Ejercicio 5 - Validación de contraseña")
    print("6. Ejercicio 6 - Análisis estadístico")
    print("7. Ejercicio 7 - Frase con vocal final")
    print("8. Ejercicio 8 - Transformación de nombre")
    print("9. Ejercicio 9 - Escala de Richter")
    print("10. Ejercicio 10 - Estaciones del año")
    print("0. Salir")
    print("="*50)

def ejercicio_1():
    """
    EJERCICIO 1:
    Solicita la edad del usuario y determina si es mayor de edad.
    Condición simple: if edad > 18
    """
    print("\n" + "="*50)
    print("EJERCICIO 1 - MAYOR DE EDAD")
    print("="*50)
    
    edad = int(input("Ingrese su edad: "))
    if edad > 18:
        print("Es mayor de edad")

def ejercicio_2():
    """
    EJERCICIO 2:
    Solicita la nota del usuario y determina si está aprobado (nota >= 6).
    Estructura if-else básica.
    """
    print("\n" + "="*50)
    print("EJERCICIO 2 - APROBADO/DESAPROBADO")
    print("="*50)
    
    nota = float(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def ejercicio_3():
    """
    EJERCICIO 3:
    Valida si el número ingresado es par usando el operador módulo (%).
    El número es par si el resto de la división por 2 es 0.
    """
    print("\n" + "="*50)
    print("EJERCICIO 3 - NÚMEROS PARES")
    print("="*50)
    
    numero = int(input("Ingrese un número par: "))
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

def ejercicio_4():
    """
    EJERCICIO 4:
    Clasifica al usuario en categorías según su edad usando if-elif-else.
    Rangos: <12 (niño), 12-17 (adolescente), 18-29 (joven), >=30 (adulto).
    """
    print("\n" + "="*50)
    print("EJERCICIO 4 - CATEGORÍAS POR EDAD")
    print("="*50)
    
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

def ejercicio_5():
    """
    EJERCICIO 5:
    Valida que la contraseña tenga entre 8 y 14 caracteres usando len().
    Muestra mensaje según cumpla o no con el requisito de longitud.
    """
    print("\n" + "="*50)
    print("EJERCICIO 5 - VALIDACIÓN DE CONTRASEÑA")
    print("="*50)
    
    contraseña = input("Ingrese una contraseña (8-14 caracteres): ")
    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_6():
    """
    EJERCICIO 6:
    Analiza una lista de números aleatorios para determinar el sesgo estadístico.
    Compara moda, mediana y media para identificar sesgo positivo, negativo o ninguno.
    Usa el módulo statistics de Python.
    """
    print("\n" + "="*50)
    print("EJERCICIO 6 - ANÁLISIS ESTADÍSTICO")
    print("="*50)
    
    from statistics import mode, median, mean
    import random

    numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
    print(f"Lista generada: {numeros_aleatorios}")

    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    print(f"\nModa: {moda}, Mediana: {mediana}, Media: {media:.2f}")

    if media > mediana > moda:
        print("Sesgo positivo o a la derecha")
    elif media < mediana < moda:
        print("Sesgo negativo o a la izquierda")
    else:
        print("Sin sesgo")

def ejercicio_7():
    """
    EJERCICIO 7:
    Verifica si una frase termina en vocal y añade signo de exclamación en ese caso.
    Usa indexación negativa para acceder al último carácter y verifica si está en vocales.
    """
    print("\n" + "="*50)
    print("EJERCICIO 7 - FRASE CON VOCAL FINAL")
    print("="*50)
    
    frase = input("Ingrese una frase o palabra: ")
    vocales = ['a', 'e', 'i', 'o', 'u']
    if frase[-1].lower() in vocales:
        print(frase + "!")
    else:
        print(frase)

def ejercicio_8():
    """
    EJERCICIO 8:
    Transforma un nombre según la opción seleccionada (mayúsculas, minúsculas o título).
    Usa los métodos upper(), lower() y title() de strings.
    """
    print("\n" + "="*50)
    print("EJERCICIO 8 - TRANSFORMACIÓN DE NOMBRE")
    print("="*50)
    
    nombre = input("Ingrese su nombre: ")
    print("\nOpciones de transformación:")
    print("1. Mayúsculas (PEDRO)")
    print("2. Minúsculas (pedro)")
    print("3. Título (Pedro)")
    
    opcion = input("\nSeleccione una opción (1-3): ")
    if opcion == "1":
        print(nombre.upper())
    elif opcion == "2":
        print(nombre.lower())
    elif opcion == "3":
        print(nombre.title())
    else:
        print("Opción no válida")

def ejercicio_9():
    """
    EJERCICIO 9:
    Clasifica un terremoto según la escala de Richter usando múltiples condiciones.
    Usa una serie de elif para cubrir todos los rangos de magnitud.
    """
    print("\n" + "="*50)
    print("EJERCICIO 9 - ESCALA DE RICHTER")
    print("="*50)
    
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

def ejercicio_10():
    """
    EJERCICIO 10:
    Determina la estación del año según hemisferio, mes y día ingresados.
    Usa condiciones compuestas para verificar rangos de fechas exactos.
    Considera los cambios de estación que ocurren alrededor del 21 de cada mes.
    """
    print("\n" + "="*50)
    print("EJERCICIO 10 - ESTACIONES DEL AÑO")
    print("="*50)
    
    hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
    mes = int(input("Ingrese el mes (1-12): "))
    dia = int(input("Ingrese el día (1-31): "))
    
    # Verificamos en qué rango de fechas estamos
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    
    if hemisferio == "N":
        print(f"Estación actual: {estacion_norte}")
    elif hemisferio == "S":
        print(f"Estación actual: {estacion_sur}")
    else:
        print("Hemisferio no válido")

# Programa principal
def main():
    """Controla la ejecución del programa mostrando el menú y gestionando las opciones"""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione un ejercicio (1-10) o 0 para salir: ")
        
        if opcion == "0":
            print("\n¡Gracias por usar el programa! ¡Hasta luego!")
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
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 10 o 0 para salir.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()