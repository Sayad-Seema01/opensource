a,b,c,d=list(map(int,input().split()))
if (a+b)>=d or (b+c)>=d or (c+a)>=d:
    print("YES")
else:
    print("NO")
