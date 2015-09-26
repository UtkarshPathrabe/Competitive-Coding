from fractions import gcd
import sys
t=int(sys.stdin.readline())
while t:
    n=int(sys.stdin.readline())
    if n&1:
        start = (3*n+1)//2
        st = (n-1)//2
        end = (3*n - n +2)//2
        total = 6*n*n*n
        result = start + 2*(((start-1)*start)//2 - ((end-1)*end)//2)
        result = result + st + (st-1)*st
        g= gcd(total,result)
        l=""
        l=l+str(result//g)+"/"+str(total//g)
        print (l)
    else :
        start = (3*n+1)//2
        st = (n-1)//2
        end = (3*n - n +2)//2
        total = 6*n*n*n
        result =2*(((start+1)*start)//2 - ((end-1)*end)//2)
        result = result + st*(st+1)
        g= gcd(total,result)
        l=""
        l=l+str(result//g)+"/"+str(total//g)
        print (l)
    t-=1
