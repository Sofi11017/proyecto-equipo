def multiplicar_dos_numeros():
    while True:
        try:
            linea1 = input("Introduce el primer número: ")
            num1 = float(linea1)
            break
        except ValueError:
            print("Error: El valor ingresado no es un número. Intente de nuevo.")

    while True:
        try:
            linea2 = input("Introduce el segundo número: ")
            num2 = float(linea2)
            break
        except ValueError:
            print("Error: El valor ingresado no es un número. Intente de nuevo.")

    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
    return resultado

# Ejecución de la función
multiplicar_dos_numeros()