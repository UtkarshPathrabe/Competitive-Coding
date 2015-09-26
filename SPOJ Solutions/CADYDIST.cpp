#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

int lesst (const void * a, const void * b){
  return (( *(long long*)a - *(long long*)b )<0);
}
int greatt (const void * a, const void * b){
  return (( *(long long*)b - *(long long*)a )<0);
}

int main(){
    long long N,c,p,t,cz,pz;
    long long C[100001];
    long long P[100001];
    for(int i=0;i<=100000;i++){ C[i]=0; P[i]=0; }
    scanf("%lld",&N);
    while(N!=0){
        t=0,cz=0;pz=0;
        for(int i=0;i<N;i++){
            scanf("%lld",&c);
            C[cz++]=c;
        }
        for(int i=0;i<N;i++){
            scanf("%lld",&p);
            P[pz++]=p;
        }
        qsort(C,cz,sizeof(long long), lesst);
        qsort(P,pz,sizeof(long long), greatt);
        for(int i=0;i<cz;i++){
            //cout<<P[i]<<" "<<C[i]<<endl;
            t+=C[i]*P[i];
            C[i]=0;
            P[i]=0;
        }
        printf("%lld\n",t);
        scanf("%lld",&N);
    }
    return 0;
}
