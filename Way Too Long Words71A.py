p=int(input())

for i in range(p):
    q=input()
    r=len(q)
    if r>10:
        print(q[0]+str(r-2)+q[r-1])
        
    else:
        print(q)
