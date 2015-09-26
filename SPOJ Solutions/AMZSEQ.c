#include <stdio.h>
 
int a[3]={1,1,1};
int p[3]={1,1,1};
 
int main(){
	int n;
	scanf("%d", &n);
	while(--n){
		a[0]=p[0]+p[1];
		a[1]=p[0]+p[1]+p[2];
		a[2]=p[1]+p[2];
		
		p[0]=a[0];
		p[1]=a[1];
		p[2]=a[2];
	}
	printf("%d\n", a[0]+a[1]+a[2]);
	return 0;
}
