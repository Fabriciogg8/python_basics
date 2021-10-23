def run():
    n= int(input(""))
    s = set()
    num = input("")
    for i in num.split(" "):
        i = int(i) 
        s.add(i)

    lista = list(s)
    if len(lista) == n:   
        largo = int(input(""))
        for word in range(0,largo):
            word = input("")
            my_list = []

            for i in word.split(' ', 1):
                my_list.append(i)
            if my_list[0] == "pop":
                s.pop()
            elif my_list[0] == "remove":
                my_list[1] = int(my_list[1])
                if 0 < my_list[1] <=9:
                    s.remove(my_list[1])
            elif my_list[0] == "discard":
                my_list[1] = int(my_list[1])
                if 0 < my_list[1] <=9:
                    s.discard(my_list[1])
            my_list.clear()

    print(sum(s))           
    
        
if __name__ == "__main__":
    run()