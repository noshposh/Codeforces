f=int(input())
nosh=0
for i in range(f):
    l=list(map(int,input().split()))
    cnt=0
    for j in l:
        if j==1:
            cnt+=1
        
        
    if cnt>1:
        nosh+=1
        
print(nosh)
