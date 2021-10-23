def run():
    autenticacion=True
    contrasena = input("Ingresa una contrasena: ")
    for i in contrasena:
        if i == " " or len(contrasena) < 8:           
            autenticacion=False
    if autenticacion == False:
        print("Contrasena errónea")
    else:
        print("Contrasena ok")


if __name__ == "__main__":
    run()