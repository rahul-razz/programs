# Task - Take an integer input and make an arrow 

a="A"
x=int(input("Enter width " ))
for i in range (1,2*x,2):
    print((i*a).center(2*x))
for i in range (x*2):
    print((((x+1)//2)*a).center(2*x))




    
    
