mi_diccionario = {"Michael":"Jordan", "Temporadas":{"Ganadas":[1992,1993,1996,1997,1998]}}



def run():
    print(mi_diccionario["Temporadas"]["Ganadas"][len(mi_diccionario["Temporadas"]["Ganadas"])-1])
    print(len(mi_diccionario["Temporadas"]["Ganadas"]))
    print(mi_diccionario["Temporadas"]["Ganadas"][0])

if __name__ == "__main__":
    run()

    