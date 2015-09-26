#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define LEN 72
LL pre_com[100], p[100];
void pre(){
    pre_com[1] = 1;
    pre_com[2] = 2;
    pre_com[3] = 4;
    pre_com[4] = 7;
    int i=4;
    while(pre_com[i] <=1000000000000000LL)
    {
        i++;
        p[i] = p[i-2]+1;
        pre_com[i] =pre_com[i-1] + pre_com[i-2]+1;
    }
}
int find(LL n)
{
    int low=0,high=LEN,mid;
    mid = (low + high)>>1;
    while(true)
    {
        mid = (low + high)>>1;
        if(pre_com[mid] < n)
        {
            if(pre_com[mid + 1] >n)
                return mid;
            else
                low = mid;
        }
        else
        {
            if(pre_com[mid - 1] < n)
                return mid - 1;
            else
                high = mid;
        }
    }
}
void print(LL n)
{
    bool a[80]={false};
    int pos  = find(n);
    int max = pos + 1;
    a[pos+1]=true;
    LL diff = n - pre_com[pos] - 1;
    while(diff>0)
    {
        pos = find(diff);
        a[pos+1] = true;
        diff = diff - pre_com[pos] - 1;
    }
    for(int i=max ;i>=1;i--)
        if(a[i])
            printf("1");
        else
            printf("0");
}
int main()
{
    pre();
    int t;
    scanf("%d",&t);
    while(t--)
    {
        LL n;
        scanf("%lld",&n);
        print(n);
        printf("\n");
    }
    return 0;
}
