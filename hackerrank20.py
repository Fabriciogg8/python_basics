# def run():
#     A = []
#     without_duplicates = []
#     total_students= int(input(""))
#     if 2 <= total_students <= 10:
#         num = input("")
#         for element in num.split(" "):
#             element = int(element)
            
#             A.append(element)
            
#             for element in A:
#                 if element not in without_duplicates:
#                     without_duplicates.append(element)
            
#         without_duplicates.sort()
#         without_duplicates.pop()
#         print(without_duplicates[-1])

# if __name__ == "__main__":
#     run()

## OTRA FORMA DE HACERLO!!

def run(n, arr):
    A = []
    if 2 <= n <= 10:
        for element in arr:
            if element not in A:
                A.append(element)
            
        A.sort()
        A.pop()
        print(A[-1])



if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    run(n,arr)