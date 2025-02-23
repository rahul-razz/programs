#Task - Print factorial of any number

#Recursion
def factorial(n):
    if (n==0 or n==1):
        return(1)
    else:
        return n*factorial(n-1)
print(factorial(3))

#Loop 
n=int(input())
a=1
for i in range(1,n+1):
    a=a*i
print(a)

