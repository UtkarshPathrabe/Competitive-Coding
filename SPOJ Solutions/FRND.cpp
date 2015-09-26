#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,temp,t;
    long long bit[30]={0};
    cin>>n;
    t=n;
    if(n==1)
    {
        cin>>temp;
        cout<<temp;
        return 0;
    }
    while(t--){
        cin>>temp;
        for(int i=0;i<20;i++)
        {
            if((temp>>i) & 1)
                bit[i]++;
        }
    }
    long long res=0;
    for(int i=0;i<20;i++){
        res+=bit[i] * (n-bit[i])* (1<<i);
    }
    cout<<res;
    return 0;
}
