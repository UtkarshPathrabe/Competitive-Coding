#include<stdio.h>
int main(){
    int t;
	long long n;
    scanf("%i", &t);
    while(t--){
        scanf("%lli", &n);
        (n%3) ? printf("0\n") : printf("%lld\n", n/3);
    }
    return 0;
}