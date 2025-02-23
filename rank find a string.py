string=input()
sub_string=input()
a=0
i=0
for j in range(len(string)):
    if string[i:len(sub_string)+i]==sub_string:
        a=a+1
    i=i+1
print(a)