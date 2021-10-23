def run():
    largo= int(input(""))
    if 0 < largo < 1000:
        countries = set()
        for i in range(0,largo):
            i = input("")
            countries.add(i)
        print(len(countries))
 

if __name__ == "__main__":
    run()