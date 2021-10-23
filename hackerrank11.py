def run():
    M= input("")
    valuesA = []
    a = input('')
    for num in [int(n) for n in a.split(" ")]:
        valuesA.append(num)
    a = set(valuesA)


    N = input("")
    valuesB = []
    b = input('')
    for num in [int(n) for n in b.split(" ")]:
        valuesB.append(num)
    b = set(valuesB)


    final_set = a ^ b
    final_set = sorted(final_set)
    for i in final_set:
        print(i)


if __name__ == "__main__":
    run()