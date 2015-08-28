/* Time Complexity: O(n*k); Space Complexity: O(k) */

#include <bits/stdc++.h>

using namespace std;

long long int min (long long int a, long long int b) {
	return (a < b) ? a : b;
}

long long int binomialCoeff (long long int n, long long int k) {
	long long int* C = (long long int*) calloc (k+1, sizeof(long long int));
	C[0] = 1;
	for (long long int i = 1; i <= n; i++) {
		for (long long int j = min(i, k); j > 0; j--) {
			C[j] = C[j] + C[j-1];
		}
	}
	long long int result = C[k];
	free(C);
	return result;
}

int main (void) {
	long long int n = 10, k = 5;
	cout << "Value of C(" << n << ", " << k << ") is " << binomialCoeff (n, k) << "." << endl;
	return 0;
}
