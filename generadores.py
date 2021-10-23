def run(*ciudades):
    for elemento in ciudades:
        yield from elemento[3]
    
      
if __name__ == "__main__":
    print(next(run("Montevideo","Canelones")))

