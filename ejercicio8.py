def run():
    num1 = int(input("Ingresa un numero positivo por favor: "))
    list= []
    while num1 > 0:
        print(f"Perfecto {num1} es positivo")
        list.append(num1)
        num1 = int(input("Ingresa un numero positivo por favor: "))
    print(f"Se termino el programa porque {num1} es negativo") 
    suma = sum(list)
    print(f"La suma de todos los numeros de la lista es la siguiente {suma}")


if __name__ == "__main__":
    run()