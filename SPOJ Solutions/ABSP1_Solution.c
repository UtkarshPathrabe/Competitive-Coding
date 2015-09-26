#include <stdio.h>

int main(){
	int T;
	scanf("%d", &T);
	while(T--){
		int N, i;
		scanf("%d", &N);
		long long int A[N], sum = 0;
		for(i=0;i<N;i++){
			scanf("%lld", &A[i]);
		}
		for(i=0;i<N/2;i++){
			sum += (N - 2*i - 1)*(A[N-i-1]-A[i]);
		}
		printf("%lld\n", sum);
	}
	return 0;
}
