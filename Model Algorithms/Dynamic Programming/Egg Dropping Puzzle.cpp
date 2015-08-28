/* Time Complexity: O(n*(k^2)); Space Complexity: O(n*k) */

#include <bits/stdc++.h>

using namespace std;

int eggDrop (int n, int k) {
	int eggFloor[n+1][k+1];
	for (int i = 1; i <= n; i++) {
		eggFloor[i][1] = 1;
		eggFloor[i][0] = 0;
	}
	for (int i = 1; i <= k; i++) {
		eggFloor[1][i] = i;
	}
	for (int i = 2; i <= n; i++) {
		for (int j = 2; j <= k; j++) {
			eggFloor[i][j] = INT_MAX;
			for (int x = 1; x <= j; x++) {
				eggFloor[i][j] = min (1 + max (eggFloor[i-1][x-1], eggFloor[i][j-x]), eggFloor[i][j]);
			}
		}
	}
	return eggFloor[n][k];
}

int main (void) {
	int n = 2, k = 36;
	cout << "Minimum number of trials in worst case with " << n << " eggs and " << k << " floors is " << eggDrop (n, k) << "." << endl;
	return 0;
}
