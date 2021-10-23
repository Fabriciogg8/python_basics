def run():
    arroba = 0
    punto = 0
    email = input("Ingresa tu dirección de email: ")
    for i in email:
        if i == "@":           
            arroba += 1
        # acordarse que no va elif, va if porque debe evaluar las dos condiciones
        if i == ".":           
            punto += 1        
    if arroba == 1 and punto >= 1:
        print("Email valido")
    else:
        print("Email invalido")


if __name__ == "__main__":
    run()
    email = "fabricio"
    print(range(len(email)))