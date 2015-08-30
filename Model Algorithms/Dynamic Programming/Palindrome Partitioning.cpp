/* Time Complexity: O(n^2); Space Complexity: O(n^2) */

#include <bits/stdc++.h>

using namespace std;

int MPP (string str) {
	int n = str.length();
	int C[n];
	bool P[n][n];
	for (int i = 0; i < n; i++) {
		P[i][i] = true;
	}
	for (int l = 2; l <= n; l++) {
		for (int i = 0; i < n-l+1; i++) {
			int j = i+l-1;
			if (l == 2) {
				P[i][j] = (str[i] == str[j]);
			} else {
				P[i][j] = ((str[i] == str[j]) && (P[i+1][j-1]));
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (P[0][i] == true) {
			C[i] = 0;
		} else {
			C[i] = INT_MAX;
			for (int j = 0; j < i; j++) {
				if ((P[j+1][i] == true) && (C[i] > 1 + C[j])) {
					C[i] = 1 + C[j];
				}
			}
		}
	}
	return C[n-1];
}

int main (void) {
	string str = "ababbbabbababa";
	cout << "Minimum cuts needed for Palindrome Partitioning are " << MPP (str) << "." << endl;
	return 0;
}
