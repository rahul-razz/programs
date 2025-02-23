#Task - Edit a string (inputs - string, character & position)

a=input("Enter string ")
b=int(input("Enter position "))
c=input("Enter character ")

def edit_str(string,position,character):
    a=list(string)
    a[position]=character
    b="".join(a)
    print(b)

edit_str(a,b,c)