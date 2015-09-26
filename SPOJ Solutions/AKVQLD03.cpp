#include<iostream>
#include<queue>
#include<stack>
#include<algorithm>
#include<stdio.h>

using namespace std;
#define LL long long
int MAX=0;
LL a[1000009];

void update(LL a[],int idx,int val)
{
    while(idx <= MAX)
    {
        a[idx]+=val;
        idx+=(idx & -idx);
    }
}
LL query(LL a[],int idx)
{
    LL sum = 0;
    while(idx>0)
    {
        sum+=a[idx];
        idx-=(idx & -idx);
    }
    return sum;
}
int main()
{
    int n,q;
    scanf("%d%d",&n,&q);
    MAX = n;
    while(q--)
    {
        char s[10];
        int i,j;
        scanf("%s",s);
        if(s[0] == 'f')
        {
            scanf("%d%d",&i,&j);
            printf("%lld\n",query(a,j)-query(a,i-1));
        }
        else{
            scanf("%d%d",&i,&j);
            update(a,i,j);
        }
    }
    return 0;
}
