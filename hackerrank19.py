def run(x,y,z,n):
   matrix = [[j,k,i] for j in range(0,x+1) for k in range(0,y+1) for i in range(0,z+1) if j + k + i != n ]
   print(matrix)

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    run(x,y,z,n)