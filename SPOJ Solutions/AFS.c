#include <stdio.h>
#define N 1000000

long long int list[N];
long long int sequence[N];

void pre(){
	int i, j, num;
	for(i=0;i<N;i++){
		list[i] = 1;
		sequence[i] = 0;
	}
	for(i=2;i<N;i++){
		j = 2;
		while((num = i*j) < N){
			list[num] += i;
			j++;
		}
	}
	for(i=2;i<N;i++){
		sequence[i] = sequence[i-1] + list[i];
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
