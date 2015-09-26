#include <stdio.h>
int main(){
    int N, ans=0, i;
    scanf("%d", &N);
    for(i=1;i<=N/i;i++){
        ans += N / i - i + 1;
    }
    printf("%d\n", ans);
    return 0;
}