#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, m;
	cin >> n;
	int a[n+1];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	cin >> m;
	int b[m+1];
	for (int i = 0; i < m; i++) {
		cin >> b[i];
	}
	for (int i = 0; i < n; i++) {
		if (a[i] == b[i]) {
			cout << i+1 << " ";
		}
	}
	cout << endl;
	return 0;
}
