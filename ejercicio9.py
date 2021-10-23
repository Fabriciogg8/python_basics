def run():
    email= input("Ingresa tu email por favor: ")
    while email.rfind(" ") != -1:
        email= input("Ingresa tu email por favor, sin espacios: ")
    while 1 < email.count("@") >= 2:
        email= input("Ingresa tu email por favor, con un arroba: ")
    while email.endswith("@") == True:
        email= input("El email no puede terminar con un arroba: ")
    while email.startswith("@") == True:
        email= input("El email no puede iniciar con un arroba: ")    
    print("Email igresado correctamente")


if __name__ == "__main__":
    run()