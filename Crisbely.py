def dividir(a, b):
    """
    Función que divide dos números.
    Retorna el resultado o un mensaje de error si el divisor es cero.
    """
    if b == 0:
        return "Error: No es posible dividir entre cero."
    else:
        return a / b

def ejecutar_pruebas():
    print("--- Probando función de división ---")
    
    num1, num2 = 20, 5
    resultado1 = dividir(num1, num2)
    print(f"Dividir {num1} / {num2} = {resultado1}")

    num3, num4 = 10, 3
    resultado2 = dividir(num3, num4)
    print(f"Dividir {num3} / {num4} = {resultado2:.2f}")

    num5, num6 = 8, 0
    resultado3 = dividir(num5, num6)
    print(f"Dividir {num5} / {num6} = {resultado3}")

if __name__ == "__main__":
    ejecutar_pruebas()