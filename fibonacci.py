#Task - Print fibonacci of any number

# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It typically starts with 0 and 1. The sequence looks like this:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#Recurrence relation: Each subsequent term is calculated as:
#F(n)=F(n−1)+F(n−2)
#F(n) is the nth Fibonacci number, 
#F(n−1) is the previous number, and 
#F(n−2) is the one before that.

def fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input())
print(fibonacci(n))
    