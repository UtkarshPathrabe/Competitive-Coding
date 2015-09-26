#include <bits/stdc++.h>
using namespace std;
#define LL long long 
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int h,p,a;
        scanf("%d%d%d",&h,&p,&a);
        if(h<=p){
            printf("1\n");
            continue;
        }
        double y,z,d;
        LL result=0;
        y= p - 2*a;
        z= 2*(a-h);
        d= sqrt(y*y - 4*p*z);
        result = ceil((-1*y + d)/(2*p));
        result = result + (result-1);
        printf("%lld\n",result);
    }
    return 0;
}
