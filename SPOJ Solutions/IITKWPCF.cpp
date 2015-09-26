#include <bits/stdc++.h>
using namespace std;
#define LL long long
bool check(LL n)
{
    if(n==1)
        return true;
    for(LL i=2;i*i<=(n);i++)
        if(n%i==0)
            return true;
    return false;
}
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        LL n,temp;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("0 0\n");
            continue;
        }
        if(n&1)
        {
            printf("0\n");
            continue;
        }
        n>>=1;
        map<LL,int>mp;
        map<LL,int>::iterator t;
        for(LL i=1;i*i<=n;i++)
        {
            if(n%i==0)
            {
                if(check(i)){
                    mp[i]=1;
                }
                if(check(n/i))
                    mp[n/i]=1;
            }
        }
        printf("%d ",mp.size());
        for(t=mp.begin();t!=mp.end();t++)
            printf("%lld ",t->first);
        printf("\n");
    }
    return 0;
}
