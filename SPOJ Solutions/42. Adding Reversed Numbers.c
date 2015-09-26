#include <stdio.h>
int main(){
    int N, a, b, sum, revA, revB, revS;
    scanf("%d", &N);
    while(N--){
        sum = 0, revA = 0, revB = 0, revS = 0;
        scanf("%d %d", &a, &b);
        while(a){
            revA = (revA*10) + (a%10);
            a /= 10;
        }
        while(b){
            revB = (revB*10) + (b%10);
            b /= 10;
        }
        revS = revA + revB;
        while(revS){
            sum = (sum*10) + (revS%10);
            revS /= 10;
        }
        printf("%d\n", sum);
    }
    return 0;
}