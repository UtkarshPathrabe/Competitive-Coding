#include <stdio.h>
int main(){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    while(!((a==0)&&(b==0)&&(c==0))){
        if((b-a)==(c-b)){
            printf("AP %d\n", (2*c)-b);
        }else{
            printf("GP %d\n", (c*c)/b);
        }
        scanf("%d %d %d", &a, &b, &c);
    }
    return 0;
}