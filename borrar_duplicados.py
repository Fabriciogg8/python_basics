list = [1,2,3,4,4,4,5,5,6,6,7,7,8,8,8,9,9,9,9,9,9,10]
def simple_list(list):
    new_list = []
    for numero in list:
        if numero not in new_list:
            new_list.append(numero)
    print(new_list)


if __name__ == "__main__":
    simple_list(list)    