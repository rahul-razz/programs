while True:
    try:
        num=int(input("Enter a number: "))
        if isinstance(num,int):
            break
    except Exception as e:
        print("Invalid, Try again")

if num<2:
    print("Neither prime nor composite")
else:
    for i in range(2,num):
        if num%i==0:
            print("Composite")
            break
    else:
        print("Prime")

