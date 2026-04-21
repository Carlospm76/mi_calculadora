import calculadora

def show_menu():
    print("\n=== CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

def main():
    while True:
        show_menu()
        option = input("\nSeleccione una opción: ")
        
        if option == "5":
            print("¡Hasta pronto!")
            break
            
        if option not in ["1", "2", "3", "4"]:
            print("Opción no válida")
            continue
            
        try:
            x = float(input("Primer número: "))
            y = float(input("Segundo número: "))
            
            if option == "1":
                result = calculadora.add(x, y)
                print(f"Resultado: {x} + {y} = {result}")
            elif option == "2":
                result = calculadora.subtract(x, y)
                print(f"Resultado: {x} - {y} = {result}")
            elif option == "3":
                result = calculadora.multiply(x, y)
                print(f"Resultado: {x} * {y} = {result}")
            elif option == "4":
                result = calculadora.divide(x, y)
                print(f"Resultado: {x} / {y} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
