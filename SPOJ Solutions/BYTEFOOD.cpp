#include <stdio.h>
#include <stdlib.h>
#define abs(x) ((x)>0 ? (x):-(x))
#define max(x,y) (x>y ? x:y)
#define min(x,y) (x<y ? x:y)
int main(){
	int t,tt,n,m;
	int p,q;
	long long a[1000],b[1000],c[1000],x[1000],y[1000];
	int i,j;
	long long ukupno=0,temp;
	int poredak[1002];
	int trajanje[1002];
	int bio[1000];
	int koliko;
	int mmin;
	double minx,rez;
	int xx,yy;
	int temp1,temp2,temp3,mint;
	int vrijeme;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%d %d %d %d %d",x+i,y+i,a+i,b+i,c+i);
			bio[i]=0;
		}
		scanf("%d %d",&p,&q);
		koliko=0;
		xx=p;yy=q;
		vrijeme=0;
		while(1){
			mmin=-1;
			minx=0;
			for(i=0;i<n;i++){
				if (bio[i])
				continue;
				temp1=abs(xx-x[i])+abs(yy-y[i]);
				temp2=abs(p-x[i])+abs(q-y[i]);
				if (temp1+1+temp2>m){
					bio[i]=1;
					continue;
				}
				temp3=min(max(a[i]-(vrijeme+temp1)*b[i],0),min(m-temp1-temp2,c[i]));
				if (temp3==0){
					bio[i]=1;
					continue;
				}
				rez=(double)temp3*b[i]/(temp1+temp3);
				if (mmin==-1 || rez>minx){
					mmin=i;
					minx=rez;
					mint=temp3;
				}
			}
			if (mmin==-1)
				break;
			poredak[koliko]=mmin;
			trajanje[koliko]=mint;
			m-=abs(xx-x[mmin])+abs(yy-y[mmin])+mint;
			vrijeme+=abs(xx-x[mmin])+abs(yy-y[mmin])+mint;
			xx=x[mmin];
			yy=y[mmin];
			bio[mmin]=1;
			koliko++;
		}
		printf("%d\n",tt);
		for(i=0;i<koliko;i++)
		printf("%d %d\n",poredak[i]+1,trajanje[i]);
		printf("0 0\n");
	}
	return 0;
}
