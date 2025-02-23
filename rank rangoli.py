import string
alphabets=string.ascii_lowercase
rev=alphabets[::-1]
size=int(input())
length=len(rev)-size
j=size-1
for i in range(0,size):
    list=j*"-"+rev[length:length+i+1]+alphabets[size-i:size]+j*"-"
    list="-".join(list)
    print(list)
    j=j-1
for k in range(size-1):
    list1=(k+1)*"-"+rev[length:length+i]+alphabets[size-i+1:size]+(k+1)*"-"
    list1="-".join(list1)
    print(list1)
    i=i-1
    