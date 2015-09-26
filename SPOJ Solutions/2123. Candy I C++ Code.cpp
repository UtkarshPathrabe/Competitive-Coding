#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

int main(){
    int N;
    scanf("%d",&N);
    while(N!=-1){
        int * A = new int[N];
        int sum=0;
        if(A!=0){
            for(int i=0;i<N;i++){
                scanf("%d",&A[i]);
                sum+=A[i];
            }
        }
        if(sum%N!=0){printf("-1\n");}
        else{
            int avg=sum/N,c=0;
            for(int i=0;i<N;i++){
                if(A[i]>avg)
                    c+=(A[i]-avg);
            }
            printf("%d\n",c);
        }
        delete [] A;
        scanf("%d",&N);
    }
    return 0;
}