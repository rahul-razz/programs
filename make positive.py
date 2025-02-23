# Task - Take any input from user and return positive number

def positive(n):
    if n<0:
        return (-n)
    else:
        return (n)
n=positive(int(input()))
print(n)

r=positive(int(input()))
print(r)
