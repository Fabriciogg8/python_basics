def run():
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su direccion: ")
    telefono = int(input("Ingresa su telefono: "))
    list = []
    list.append(nombre)
    list.append(direccion)
    list.append(telefono) 
    print(f"Su nombre direccion y telefono son los siguientes {list[0]}, {list[1]}, {list[2]}")
  

if __name__ == "__main__":
    run()