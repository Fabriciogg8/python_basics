def average(array):
    array = set(array)
    length = len(array)
    avg = sum(array)/length
    return round(avg,3)

#ESTA PARTE COMENTADA ESTABA BIEN PERO ME PUSIERON EN EL IF NAME LO QUE QUERIAN DE INPUT
# quantity = input("")
# values = []
# numbers = input('')
# for num in [int(n) for n in numbers.split(" ")]:
#     values.append(num)
# array = set(values)
# length = len(array)


# def run():
#     average(array)    

if __name__ == "__main__":
    n= int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)