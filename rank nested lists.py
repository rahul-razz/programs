records=[]
scores=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    scores.append(score)
    records.append([name,score])

scores=list(scores)
scores=set(scores)
scores=list(scores)
scores.sort()
second=scores[1]
out=[i[0] for i in records if i[1]==second]
out.sort()
for i in out:
    print(i)
