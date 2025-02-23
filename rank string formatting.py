def print_formatted(number):
    padding=len(bin(number)[2:])
    for i in range(1,number+1):
        octal=oct(i)[2:]
        binary=bin(i)[2:]
        hexadecimal=hex(i)[2:].upper()
        print(f"{i:>{padding}} {octal:>{padding}} {hexadecimal:>{padding}} {binary:>{padding}}")
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)