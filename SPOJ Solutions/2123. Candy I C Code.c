#include <stdio.h>
int main(){
    int N, sum, i, array[1000];
    scanf("%d", &N);
    while(N != -1){
        sum = 0;
        for(i=0;i<N;i++){
            scanf("%d", array[i]);
            sum += array[i];
        }
        if((sum/N)==0)
            printf("-1\n");
        else{
            int avg = (sum/N), c = 0;
            for(i=0;i<N;i++){
                if(array[i]>avg){
                    c += (array[i]-avg);
                }
            }
            printf("%d\n",c);
        }
        scanf("%d", &N);
    }
    return 0;
}