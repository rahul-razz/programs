# Task - If age is greater than 18 print you can drive but if between 17 and 17.25 print #you can drive in 9 months but if between 17.25 and 17.5 print can drive in 6 months but if between 17.5 and 17.75 print you can drive in 3 months and if between 17.75 and 17.9 print soon but if between 17.9 and 18 print come tomorrow

a=float(input())
if a>=18:
    print("You can drive")
elif a>=17.75 and a<18:
    if a>=17.75 and a<17.9:
        print("soon")
    else:
        print("come tomorrow")
elif a>=17.5 and a<17.75:
    print("You can drive in 6 months")
elif a>=17.25 and a<17.5:
    print("You can drive in 3 months")
elif a>=17 and a<17.25:
    print("You can drive in 9 months")
else:
    print("Beta jaake pogo dekho")
