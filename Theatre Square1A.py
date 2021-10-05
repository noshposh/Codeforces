n,m,a=list(map(int,input().split()))

if n%a==0 and m%a==0:
    p=(n//a)*(m//a)
elif (n%a) !=0 and m%a==0:
    p=((n//a)+1)*(m//a)
elif(n%a)==0 and (m%a) !=0:
    p=((m//a)+1)*(n//a)
elif (n%a) !=0 and (m%a) !=0:
    p=((m//a)+1)*((n//a)+1)
    
print(p)
