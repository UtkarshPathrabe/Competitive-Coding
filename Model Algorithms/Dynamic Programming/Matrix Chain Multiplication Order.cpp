/* Time Complexity: O(n^3); Space Complexity: O(n^2) */

#include <bits/stdc++.h>

using namespace std;

int matrixChainOrder (int p[], int n) {
	int m[n][n];
	for (int i = 0; i < n; i++) {
		m[i][i] = 0;
	}
	for (int l = 2; l < n; l++) {
		for (int i = 1; i <= n-l+1; i++) {
			int j = i+l-1;
			m[i][j] = INT_MAX;
			for (int k = i; k < j; k++) {
				m[i][j] = min (m[i][j], m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]);
			}
		}
	}
	return m[1][n-1];
}

int main (void) {
	int p[] = {1, 2, 3, 4};
	int size = sizeof (p) / sizeof (p[0]);
	cout << "Minimum number of Multiplications are " << matrixChainOrder (p, size) << "." << endl;
	return 0;
}
