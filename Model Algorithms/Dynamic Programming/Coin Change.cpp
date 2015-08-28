#include <bits/stdc++.h>

using namespace std;

int CountChangeNotSpaceOptimized (vector <int> &S, int n) {
	int m = S.size();
	int table[n+1][m];
	for (int i = 0; i < m; i++) {
		table[0][i] = 1;
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < m; j++) {
			table[i][j] = ((i-S[j] >= 0) ? table[i-S[j]][j] : 0) + ((j >= 1) ? table[i][j-1] : 0);
		}
	}
	return table[n][m-1];
}

int CountChangeSpaceOptimized (vector<int> &S, int n) {
	int m = S.size();
	int *table = (int*) calloc (n+1, sizeof(int));
	table[0] = 1;
	for (int i = 0; i < m; i++) {
		for (int j = S[i]; j <= n; j++) {
			table[j] += table[j-S[i]];
		}
	}
	return table[n];
}

int main (void) {
	vector <int> arr;
	arr.push_back (2);
	arr.push_back (5);
	arr.push_back (3);
	arr.push_back (6);
	int n = 10;
	cout << CountChangeNotSpaceOptimized (arr, n) << " Coin changes are possible for n = " << n << "." << endl;
	cout << CountChangeSpaceOptimized (arr, n) << " Coin changes are possible for n = " << n << "." << endl;
	return 0;
}
