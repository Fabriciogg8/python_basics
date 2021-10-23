def run():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))
    promedio = round((num1 + num2 + num3)/3)
    print(f"El promedio de los numero ingresados es {promedio}")
  

if __name__ == "__main__":
    run()