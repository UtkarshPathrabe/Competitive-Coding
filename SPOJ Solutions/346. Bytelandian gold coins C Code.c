#include <stdio.h>
int main(){
    int n, m;
    while(scanf("%d", &n)==1){
        m = (n/2)+(n/3)+(n/4);
        if(n < m){
            printf("%d\n", m);
        }else{
            printf("%d\n", n);   
        }
    }
    return 0;
}