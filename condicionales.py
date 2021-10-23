def run():
    edad=int(input("Ingresa tu edad: "))
    if edad > 80:
        print("Sos viejo")
    elif edad > 90: 
        print("Sos muy viejo")
    else:
        print("Sos joven")

if __name__ == "__main__":
    run()