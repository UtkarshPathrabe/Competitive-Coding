/* Time Complexity: O(n^2); Space Complexity: O(n^2) */

#include <bits/stdc++.h>

using namespace std;

int LPS (string str) {
	int n = str.length();
	int L[n][n];
	for (int i = 0; i < n; i++) {
		L[i][i] = 1;
	}
	for (int l = 2; l <= n; l++) {
		for (int i = 0; i < n-l+1; i++) {
			int j = i+l-1;
			if ((str[i] == str[j]) && (l == 2)) {
				L[i][j] = 2;
			} else if (str[i] == str[j]) {
				L[i][j] = L[i+1][j-1] + 2;
			} else {
				L[i][j] = max (L[i][j-1], L[i+1][j]);
			}
		}
	}
	return L[0][n-1];
}

int main (void) {
	string str = "GEEKS FOR GEEKS";
	cout << "The length of the longest palindromic subsequence is " << LPS (str) << "." << endl;
	return 0;
}
