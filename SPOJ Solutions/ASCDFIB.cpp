#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long bigint;
int fib[1110000];

int genfib(int n){
//	printf("%i\n", n);
	if(fib[n]!=-1)
		return fib[n];
	int k=n>>1;
	int fk=genfib(k);
	int fk1=genfib(k+1);
	if(n%2==0){
		fib[n]=((bigint)fk*((2*(bigint)fk1+1000000)-(bigint)fk))%100000;
		return fib[n];
	}else{
		fib[n]=(((bigint)fk1*(bigint)fk1)+((bigint)fk*(bigint)fk))%100000;
		return fib[n];
	}
}

int main(){
	for(int i=0; i<1110000; i++){
		fib[i]=-1;
	}
	//fib[0]=0;
	fib[0]=0;
	fib[1]=1;
	fib[2]=1;
	//for(int i=1; i<1100000; i++)
	//	printf("%lli\n", genfib(i));

	int t;
	scanf("%i", &t);
	for(int i=0; i<t; i++){
		int a, b;
		scanf("%i %i", &a, &b);
		a--;
		int *v=new int[b+1];
		for(int j=a; j<=a+b; j++){
			v[j-a]=(genfib(j));
		}
		partial_sort(v, v+100, v+b+1);
		printf("Case %i:", i+1);
		int lim=min(100, b+1);
		for(int j=0; j<lim; j++){
			printf(" %i", v[j]);
		}
		printf("\n");
	//	delete v;

	}
}
