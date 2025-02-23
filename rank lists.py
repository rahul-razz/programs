N = int(input())
l1=[]
for _ in range(N):
        cmd = map(str,input().split())
        clist=list(cmd)
        if clist[0]=="insert":
            l1.insert(int(clist[1]),int(clist[2]))
        elif clist[0]=="print":
            print(l1)
        elif clist[0]=="remove":
            l1.remove(int(clist[1]))
        elif clist[0]=="append":
            l1.append(int(clist[1]))
        elif clist[0]=="sort":
            l1.sort()
        elif clist[0]=="pop":
            l1.pop()
        elif clist[0]=="reverse":
            l1.reverse()
            
