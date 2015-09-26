import sys
t=int(sys.stdin.readline())
while t:
    n,q=map(int,sys.stdin.readline().split())
    s=raw_input().split()
    cum=[]
    cum2=[]
    for i in range(0,n+1):
        cum.append(0)
        cum2.append(0)
    for i in range(1,n+1):
        cum[i]=cum[i-1] + int(s[i-1])
        cum2[i]=cum2[i-1]+i*(int(s[i-1]))
    for i in range(0,q):
        w,x,y,z=map(int,sys.stdin.readline().split())
        lower = y+x
        higher = z+x
        result=(cum2[higher]-cum2[lower-1] + (w-x)*(cum[higher]-cum[lower-1]))%1000000007
        sys.stdout.write(str(result))
        sys.stdout.write("\n")
    t=t-1
