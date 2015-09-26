#include <bits/stdc++.h>

using namespace std;

#define ULL unsigned long long 
#define MOD 1000000007
#define INV 333333336 //Inverse modulo of 3 with 1000000007

ULL pow_mod(ULL n){
    ULL x=1,p=2;
    while(n)
    {
        if(n&1)
            x=(x*p)%MOD;
        p=(p*p)%MOD;
        n>>=1;
    }
    return x;
}
int main(){
    ULL n, result;
    while(scanf("%llu", &n) != EOF){
        if(n&1){
            result = ((pow_mod(n)+1)*INV)%MOD;
            printf("%llu\n",result);
        }
        else{
            result = ((pow_mod(n)+2)*INV)%MOD;
            printf("%llu\n",result);
        }
    }
    return 0;
}
