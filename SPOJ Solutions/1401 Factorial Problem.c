#include <stdio.h>
#include <math.h>
int main(void){
	int T, N, i, p, sum;
	scanf("%d", &T);
	while(T > 0){
		scanf("%d", &N);
		i = 1;
		sum = 0;
		p = pow(5, i);
		while(p <= N){
			sum += (N/p);
			i++;
			p = pow(5, i);
		}
		printf("%d\n", sum);
		T--;
	}
	return 0;
}