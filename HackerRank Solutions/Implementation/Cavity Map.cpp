#include <bits/stdc++.h>

using namespace std;

char ma[101][101];
int n;

int toNumber (char ch) {
	return ch - '0';
}

bool isCavity (int i, int j) {
	if ((i != 0) && (i != n-1) && (j != 0) && (j != n-1) && (toNumber(ma[i][j]) > toNumber(ma[i-1][j])) && (toNumber(ma[i][j]) > toNumber(ma[i][j-1])) && (toNumber(ma[i][j]) > toNumber(ma[i+1][j])) && (toNumber(ma[i][j]) > toNumber(ma[i][j+1]))) {
		return true;
	}
	return false;
}

int main (void) {
	cin >> n;
	char ans[n][n];
	for (int i = 0; i < n; i++) {
		cin >> ma[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (isCavity(i, j)) {
				ans[i][j] = 'X'; 
			} else {
				ans[i][j] = ma[i][j];
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << ans[i][j];
		}
		cout << endl;
	}
	return 0;
}
