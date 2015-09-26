#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n,m,x,y;
        scanf("%d%d%d%d",&n,&m,&x,&y);
        int r1,r2,r3,r4,result;
        r1 = abs(x-1) + abs(y-1);
        r2 = abs(x-1) + abs(y-m);
        r3 = abs(x-n) + abs(y-1);
        r4 = abs(x-n) + abs(y-m);
        result = max(r1,max(r2,max(r3,r4)));
        printf("%d\n",result);
    }
    return 0;
}
