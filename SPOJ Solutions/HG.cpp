#include <cstdio>
#include <iostream>

using namespace std;

long gcd(long a, long b){
	return b == 0 ? a : gcd(b, a%b);
}

long a[1009];
long b[1009];
long store[1000000];

int main(){
	int n, m;
	scanf("%d", &n);
	for(int i=0; i<n; i++)
		scanf("%ld", &a[i]);
	scanf("%d", &m);
	for(int i=0; i<m; i++)
		scanf("%ld", &b[i]);
	int k = 0;
	long g;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			g = gcd(a[i], b[j]);
			if(b[j]!=1 && g!=1){
				store[k++] = g;
				a[i] = a[i]/g;
				b[j] = b[j]/g;
			}
		}
	}
	long long temp, carry;
	long total = 1;
	int flage = 0;
	int res[10] = {0};
	res[9] = 1;
	for(int i=0; i<k; i++){
		carry = 0;
		total *= store[i];
		if(total > 999999999){
			flage = 1;
		}
		for(int j=9; j>=1; j--){
			temp = res[j] * store[i];
			res[j] = (temp + carry)%10;
			carry = (temp + carry)/10;
		}
	}
	if(flage){
		for(int i=1; i<=9; i++)
			printf("%d", res[i]);
	}else{
		printf("%ld", total);
	}
	printf("\n");
	return 0; 
}