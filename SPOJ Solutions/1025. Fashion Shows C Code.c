#include <stdio.h>
int main(){
    int t, N, i, j, temp;
    scanf("%d", &t);
    while(t--){
        scanf("%d", &N);
        int males[N], females[N];
        for(i=0;i<N;i++){
            scanf("%d", males[i]);
        }
        for(i=0;i<N;i++){
            scanf("%d", females[i]);
        }
        for(i=0;i<N;i++){
            for(j=i;j<N;j++){
                if(males[i] > males[j]){
                    temp=males[i];
                    males[i]=males[j];
                    males[j]=temp;
                }
                if(females[i] > females[j]){
                    temp=females[i];
                    females[i]=females[j];
                    females[j]=temp;
                }
            }
        }
        temp = 0;
        for(i=0;i<N;i++){
            temp += (males[i]*females[i]);
        }
        printf("%d\n", temp);
    }
    return 0;
}