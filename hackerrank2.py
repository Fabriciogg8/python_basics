'''Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example 
a=3
b=5
output: 8 -2 15 '''


def run():
    n1=int(input(""))
    n2=int(input(""))
    print(n1+n2)
    print(n1-n2)
    print(n1*n2)          
        
if __name__ == '__main__':
    run()
