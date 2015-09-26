#include <bits/stdc++.h>
using namespace std;
#define LL long long
bool a[1000009];
LL prime[80000];
int total;
void pre()
{
    for(int i=2;i<=1000;i++)
    {
        if(!a[i])
            for(int j=i*i;j<=1000000;j+=i)
                a[j]=true;
    }
    total=0;
    prime[total++]=2;
    for(int i=3;i<=1000000;i+=2)
        if(!a[i])
            prime[total++]=i;
}
int main()
{
    int t;
    pre();
    scanf("%d",&t);
    while(t--)
    {
        long long n,res=1,temp,in,count;
        int k;
        bool flag=false,flag2=false;
        scanf("%lld%d",&n,&k);
        temp=n;
        while(k--)
        {
            scanf("%lld",&in);
            if(in==1)
            {
                flag=true;
                continue;
            }
            while(temp%in == 0)
                temp/=in;
        }
        
        if(flag)
        {
            printf("0\n");
            continue;
        }
        if(temp==n)
            flag2=true;
        int l=0;
        while(prime[l]*prime[l]<=temp && l<total)
        {
            count=0;
            while(temp % prime[l] == 0)
            {
                count++;
                temp/=prime[l];
            }
            res*=count+1;
            l++;
        }
        if(temp>1)
            res*=2;
        if(flag2)
            res--;
        printf("%lld\n",res);
    }
}
