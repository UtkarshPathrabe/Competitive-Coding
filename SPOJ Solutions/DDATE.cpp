#include<stdio.h>
#include<math.h>
int j,k,N,X,l,y,d,m,r;
char *o[]={"January","February","March","April","May","June","July","August","September","October","November","December"};
main(){
	scanf("%d",&N);
	while(N--){
		scanf("%d",&X);
		j=k=l=d=m=y=0;
		while(X){
			r=X%2;
			(j<5)?(d+=r*pow(2,j++)):(k<4)?(m+=r*pow(2,k++)):(y+=r*pow(2,l++));
			X/=2;
		}
		printf("%d %s %d\n",d,o[m-1],y);
	}
	return 0;
}
