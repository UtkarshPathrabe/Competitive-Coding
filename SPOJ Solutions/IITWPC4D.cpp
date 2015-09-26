#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cfloat>
#include <map>
#include <fstream>
#include <sstream>
#include <bits/stdc++.h>
#include <climits>
using namespace std;
#define gc getchar_unlocked
inline void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
int T[1000000],A[300000],N,t,i,j,k,ans[300000];
void build(int node,int a,int b){
    int mid=(a+b)>>1;
    if(a==b) T[node]=1;
    else{
        build(node<<1,a,mid);
        build((node<<1)+1,mid+1,b);
        T[node]=b-a+1;
    }
}
int query(int node,int pos,int a,int b){
    if(a==b){
        --T[node];
        return a;
    }
    int mid=(a+b)>>1;
    --T[node];
    if(pos<=T[node<<1])   return query(node<<1,pos,a,mid);
    else return query((node<<1)+1,pos-T[node<<1],mid+1,b);
}
int main(){
    scanf("%d",&t);
    for(int j=1;j<=t ; j++){
        scanint(N);
        int flag = 1;
        for(i=0;i<N;i++){ 
            scanint(A[i]);
            if(A[i]>i)
                flag=0;}
        if(!flag)
        {
            printf("Test : %d\n",j);
            printf("-1\n");
            continue;
        }
        build(1,1,N);
        for(i=N-1;i>=0;i--) ans[i]=query(1,i-A[i]+1,1,N);
        printf("Test : %d\n",j);
        for(int i=0;i<N;i++)
            printf("%d ",ans[i]);
        printf("\n");
    }
    return 0;
}
