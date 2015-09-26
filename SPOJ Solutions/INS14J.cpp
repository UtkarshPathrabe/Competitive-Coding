#include <bits/stdc++.h>
using namespace std;
class pairM
{
public:
    int x,y,d;
    void operator =(pairM p)
    {
        x=p.x;
        y=p.y;
        d=p.d;
    }
};
inline void read(int &x) {
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;
    for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
    if(c=='-') {
        neg = 1;
        c = getchar_unlocked();}
    for(; c>47 && c<58 ; c = getchar_unlocked()) {
        x = (x<<1) + (x<<3) + c - 48;}
    if(neg)
        x = -x;
}
void merge(pairM p[],int low,int mid,int high)
{
    pairM temp[10009];
    int i=low,j=mid+1,k=low;
    while(i<=mid && j<=high)
    {
        if(p[i].d >= p[j].d)
            temp[k++] = p[i++];
        else
            temp[k++] = p[j++];
    }
    while(i<=mid)
        temp[k++] = p[i++];
    while(j<=high)
        temp[k++] = p[j++];
    for(i=low;i<=high;i++)
        p[i] = temp[i];
}
void partition(pairM p[],int low,int high)
{
    int mid;
    if(low<high)
    {
        mid = (low + high)>>1;
        partition(p,low,mid);
        partition(p,mid+1,high);
        merge(p,low,mid,high);
    }
}
int main()
{
    int t;
    read(t);
    while(t--)
    {
        int n;
        read(n);
        pairM p[10009];
        for(int i=0;i<n;i++)
        {
            read(p[i].x);
            read(p[i].y);
            p[i].d= p[i].y-p[i].x;
        }
        partition(p,0,n-1);
        long long sum=0;
        for(int i=0;i<n;i++)
            if(!(i&1)){
                sum = sum^( min(p[i].y,p[i].x));
            }
        if(sum)
            printf("Yes\n");
        else
            printf("No\n"); 
    }
    return 0;
}
