# Task - Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

'''
#My initial program

word=input("Enter word: ")

lsit=[]
for i in word:
    lsit.append(i)

command=input("Code or Decode: ")

if len(word)<3:
    lsit.sort(reverse=True)
else:
    if command=="code":
        first=lsit[0]
        lsit.pop(0)
        lsit.append(first)
        import string
        import random
        start="".join(random.choices(string.ascii_letters,k=3))
        end="".join(random.choices(string.ascii_letters,k=3))
        lsit.insert(0,start)
        lsit.append(end)
    else:
        for j in range(3):
            lsit.pop(0)
            lsit.pop()
        last=lsit[len(lsit)-1]
        lsit.pop()
        lsit.insert(0,last)
lsit="".join(lsit)
print(lsit)
'''

import string
import random

def encode(word):
    if len(word)<3:
        return word[1]+word[0]
    else:
        word=word[1:]+word[0]
        start="".join(random.choices(string.ascii_letters,k=3))
        end="".join(random.choices(string.ascii_letters,k=3))
        return start+word+end

def decode(word):
    if len(word)<3:
        return word[1]+word[0]
    else:
        word=word[3:-3]
        return word[-1]+word[0:-1]

def main():
    command=input("Enter command to code or decode: ").strip().lower()
    if command not in ['code','decode']:
        print("Enter a valid command")
        return

    word=input("Enter a word to be coded or encoded: ").strip()

    if command=="code":
        print("Encode word:",encode(word))
    
    elif command=="decode":
        print("Decoded word:",decode(word))

if __name__=="__main__":
    main()








