# Task - Make a calculator which takes 2 input and returns desired mathematical operation

x=input("Enter ")
x=int(x)
y=int(input())
command=input("Enter command: ")
if command=="+" :
    print(x+y)
if command=="-":
    if x>y:
        print(x-y)
    else:
        print(y-x)
if command=="*":
    print(x*y)
if command=="/":
    print(x/y)
