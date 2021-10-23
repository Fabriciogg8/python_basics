from functools import reduce

def multiplicar(x, y):
 return x * y


def run():
    l = range(1,150,50)
    l2 = reduce(multiplicar, l)
    print(l2)


if __name__ == "__main__":
    run()