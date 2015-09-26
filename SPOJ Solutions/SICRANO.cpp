#include<iostream>
#include<vector>
using namespace std;

struct pnt {
    float x;
    float y;
};
typedef struct pnt point;

struct ln {
    point p1;
    point p2;
};
typedef struct ln line;

bool lieson(line l, point p){
    if(((p.x==l.p1.x)&&(p.y==l.p1.y)) || ((p.x==l.p2.x)&&(p.y==l.p2.y))){ // Same point
        return true;
    }
    if(l.p1.x-l.p2.x==0){ // parallel to Y axis
        if(p.x==l.p1.x && (p.y-l.p1.y)*(p.y-l.p2.y)<0){
            return true;
        }else{//cout<<"f1\n";
            return false;
        }
    }
    if(l.p1.y-l.p2.y==0){ // Parallel to X-axis
        if(p.y==l.p1.y && (p.x-l.p1.x)*(p.x-l.p2.x)<0){
            return true;
        }else{//cout<<"f2\n";
            return false;
        }
    }
    if((p.x==l.p1.x)||(p.y==l.p1.y)||(p.x==l.p2.x)||(p.y==l.p2.y)){ // Parallel to none of axes but have same one cooordinate
        //cout<<"f3"<<endl;
        return false;
    }
    if( ((p.y-l.p1.y)/(p.x-l.p1.x))==((l.p1.y-l.p2.y)/(l.p1.x-l.p2.x)) ){
        if((p.x-l.p1.x)*(p.x-l.p2.x)<=0){
            //cout<<(l.p1.x-l.p2.x)/(l.p1.y-l.p2.y)<<endl;
            return true;
        }else{//cout<<"f4\n";
            return false;
        }
    }else{//cout<<"f5\n";
        return false;
    }
}

int main(){
    int T,N,M;
    float x,y,x1,y1,x2,y2;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>N>>M;
        vector<point> P;
        vector<line> L;
        for(int j=0;j<N;j++){
            cin>>x>>y;
            point p;
            p.x=x;
            p.y=y;
            P.push_back(p);
        }
        //cout<<"points"<<endl;
        for(int j=0;j<M;j++){
            cin>>x1>>y1>>x2>>y2;
            line l;
            l.p1.x=x1;
            l.p1.y=y1;
            l.p2.x=x2;
            l.p2.y=y2;
            L.push_back(l);
            int s=0;
            for(int k=0;k<N;k++){ //cout<<lieson(l,P[k])<<endl;;
                if(lieson(l,P[k])) s++;
            }
            cout<<s<<endl;
        }
        //cout<<"lines"<<endl;
    }
    return 0;
}
