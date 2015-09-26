#include <stdio.h>
int main(){
    long int N, sum, i, temp, t;
    scanf("%ld", &t);
    while(t--){
        sum = 0;
        scanf("%ld", &N);
        for(i=0;i<N;i++){
            scanf("%ld",&temp);
            sum =sum+temp;
            sum=sum%N;
        }
        if(sum==0)
            printf("Yes\n");
        else{
            printf("No\n");
        }
    }
    return 0;
}