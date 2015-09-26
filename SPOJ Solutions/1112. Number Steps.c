#include <stdio.h>
int main(){
    int N, x, y, p;
    scanf("%d", &N);
    while(N--){
        p = 0;
        scanf("%d %d", &x, &y);
        if((x==y) || ((y+2)==x)){
            if((y%2)==0){
                p = x + y;
            }else{
                p = (x + y) - 1;
            }
            printf("%d\n", p);
        }else{
            printf("No Number\n");
        }
    }
    return 0;
}