#include <stdio.h>

int main(void){
    int t, m, n, i, j, flag;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d", &m, &n);
        for(i = m; i <= n; i++){
            if(i <= 1){
                i = 2;
            }
            flag = 0;
            for(j = 2; j <= i/2; j++){
                if(i%j==0){
                    flag = 1;
                    break;
                }
            }
            if(!flag){
                printf("%d\n", i);
            }
        }
        printf("\n");
    }
    return 0;
}