# Enter your code here. Read input from STDIN. Print output to STDOUT
total_shoes=int(input())
sizes=map(int,input().split())
sizes=list(sizes)
customers=int(input())
sum=0
for i in range(customers):
    size,money=input().split()
    if int(size) in sizes:
        sum=sum+int(money)
        sizes.remove(int(size))
print(sum)
