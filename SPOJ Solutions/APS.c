#include <stdio.h>
#define N 10000000

int smallestPrime[N];
long long int sequence[N];

void pre(){
	int i, j;
	for(i=0;i<N;i++){
		smallestPrime[i] = 0;
		sequence[i] = 0;
	}
	for(i=2;i<N;i++){
		if(!smallestPrime[i]){
			for(j=i+i;j<N;j+=i){
				if(!smallestPrime[j]){
					smallestPrime[j] = i;
				}
			}
			sequence[i] = sequence[i-1] + i;
		}else{
			sequence[i] = sequence[i-1] + smallestPrime[i];
		}
	}
}

int main(){
	int t;
	scanf("%d", &t);
	pre();
	while(t--){
		int n;
		scanf("%d", &n);
		printf("%lld\n", sequence[n]);
	}
	return 0;
}
