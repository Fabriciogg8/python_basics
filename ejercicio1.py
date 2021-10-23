def run():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el primer numero: "))
    print(f"Comprobaremos cual es el numero mayor entre {num1} y {num2}")
    if num1 > num2:
        print("El primer numero es mayor")
    elif num1 == num2:
        print("Los numeros son iguales")
    else:
        print("El segundo numero es mayor")


if __name__ == "__main__":
    run()