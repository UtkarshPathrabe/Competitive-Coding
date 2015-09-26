#include <stdio.h>

int min(int a, int b){
	if(a >= b)
		return b;
	else
		return a;
}

int main(){
	int tc = 1, N, a, b, c, dp[2][3];
	while(1){
		scanf("%d", &N);
		if(N==0)
			break;
		scanf("%d %d %d", &a, &b, &c);
		dp[0][0] = 100000000;
		dp[0][1] = b;
		dp[0][2] = b+c;
		int i, r;
		for(i=1,r=1;i<N;++i,r=!r){
			scanf("%d %d %d", &a, &b, &c);
			dp[r][0] = a + min(dp[!r][0], dp[!r][1]);
			dp[r][1] = b + min(min(dp[!r][0], dp[r][0]), min(dp[!r][1], dp[!r][2]));
			dp[r][2] = c + min(dp[!r][2], min(dp[!r][1], dp[r][1]));
		}
		printf("%d. %d\n", tc++, dp[(N-1) & 1][1]);
	}
	return 0;
}
