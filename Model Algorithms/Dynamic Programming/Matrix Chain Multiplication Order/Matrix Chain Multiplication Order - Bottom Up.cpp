/* Author: Utkarsh Ashok Pathrabe
*  Problem Statement: Matrix Chain Multiplication Order
*/

/* Time Complexity: Omega(n^3)
*  Space Complexity: Theta(n^2)
*/

#include <bits/stdc++.h>
#define N 100

using namespace std;

vector<int> p;
int n;
int m[N][N] = {{0}}, s[N][N] = {{0}};

void PrintOptimalParens (int i, int j) {
	if (i == j) {
		cout << "A[" << i << "]"; 
	} else {
		cout << "(";
		PrintOptimalParens (i, s[i][j]);
		PrintOptimalParens (s[i][j] + 1, j);
		cout << ")";
	}
}

int MatChainOrder () {
	for (int i = 1; i <= n; i++) {
		m[i][i] = 0;
	}
	for (int l = 2; l <= n; l++) {
		for (int i = 1; i <= n - l + 1; i++) {
			int j = l + i - 1;
			m[i][j] = INT_MAX;
			for (int k = i; k < j; k++) {
				int q = m[i][k] + m[k+1][j] + (p[i-1]*p[k]*p[j]);
				if (q < m[i][j]) {
					m[i][j] = q;
					s[i][j] = k;
				}
			}
		}
	}
	return m[1][n];
}

int main (void) {
	cout << "Enter the number of matrices: \t";
	cin >> n;
	for (int i = 0; i <= n; i++) {
		int temp;
		cin >> temp;
		p.push_back(temp);
	}
	cout << MatChainOrder () << endl;
	PrintOptimalParens (1, n);
	cout << endl;
	return 0;
}
