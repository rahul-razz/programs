dict={}
a=int(input())
for _ in range(a):
    name,*line=input().split()
    scores=list(map(float,line))
    dict.update({name:scores})
query=input()
sample=dict[query]
sum=0
for i in sample:
    sum=sum+i
avg=sum/len(sample)
average=f"{avg:.2f}"
print(average)
