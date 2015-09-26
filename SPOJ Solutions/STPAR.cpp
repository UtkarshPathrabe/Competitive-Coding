#include<iostream>
#include<queue>
#include<stack>
#include<algorithm>
#include<stdio.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    while(n!=0){
        int v;
        queue<int> Q;
        stack<int> S;
        for(int i=0;i<n;i++){
            cin>>v;
            Q.push(v);
        }

        //printf("QSstart\n");
        int c=1;
        while(!Q.empty()||!S.empty()){
            //printf("QS\n");
            if(!Q.empty()&&Q.front()==c) {
            //printf("Qf\n");
                Q.pop();
                c++;
            }else{
                if(!S.empty()&&S.top()==c){
                    //printf("Sf\n");
                    S.pop();
                    c++;
                }else{
                    if(!Q.empty()){
                    //printf("Q\n");
                        int s=Q.front();
                        S.push(s);
                        Q.pop();
                    }else{
                        break;
                    }
                }
            }
        }
        if(c==n+1){
            cout<<"yes"<<endl;
        }else{
            cout<<"no"<<endl;
        }
        //printf("QSend\n");
        cin>>n;
    }
    return 0;
}
