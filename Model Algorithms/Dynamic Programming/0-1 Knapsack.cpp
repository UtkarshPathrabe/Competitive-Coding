/* Time Complexity: O(n*W); Space Complexity: O(W) */

#include <bits/stdc++.h>
#define LLI long long int

using namespace std;

long long int max (long long int a, long long int b) {
	return (a > b) ? a : b;
}

LLI knapSack (LLI W, LLI wt[], LLI val[], LLI n) {
	LLI *KS = (LLI*) calloc (W+1, sizeof(LLI));
	for (LLI i = 1; i <= n; i++) {
		for (LLI w = W; w > 0; w--) {
			if (wt[i-1] <= w) {
				KS[w] = max (val[i-1] + KS[w-wt[i-1]], KS[w]);
			}
		}
	}
	LLI result = KS[W];
	free(KS);
	return result;
}

int main (void) {
	LLI val[] = {60, 100, 120};
	LLI wt[] = {10, 20, 30};
	LLI W = 50;
	LLI n = sizeof (val) / sizeof (val[0]);
	cout << "Maximum Value of Knap Sack is " << knapSack (W, wt, val, n) << "." << endl;
	return 0;
}
