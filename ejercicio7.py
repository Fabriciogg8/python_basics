def run():
    num1 = int(input("Ingresa un numero por favor: "))
    num2 = int(input("Ingresa un numero por favor, mayor al anterior: "))
    while num1 < num2:
        print(f"Perfecto {num2} es mayor que {num1}")
        num1 = num2
        num2 = int(input("Ingresa un numero mayor al anterior por favor: "))
    print(f"Se termino el programa porque {num2} es menor que {num1}")


if __name__ == "__main__":
    run()