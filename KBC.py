# Task - Make two lists. One of question and other of answers and play KBC taking input from user

list=["Capital of India", "Prime minister", "Richest person", "Most handsome Man"]
list2=["Delhi", "Modi", "Ambani", "Harry sir"]
i=0
j=0
k=1
amount=0
for i in list:
    print(i)
    ans=input()
    if ans==list2[j]:
        print("Correct")
        amount=amount+1000*k
        k=k+1
        print("Congrats you have won",amount)
    else:
        print("Sorry but Incorrect")
        print("The correct answer was",list2[j])
    j=j+1
print("Total you have won",amount)
