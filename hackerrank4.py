'''Task
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i2.

Example
n=3
The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line.'''


def run():
    n1=int(input(""))
    if 0<= n1 <= 20:
        for i in range(0,n1):
            print(i**2)
            
        
if __name__ == '__main__':
    run()
