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
	int i, j;
	for (i = 0, j = 0; (i < n) && (j < m); ) {
		if (a[i] > b[j]) {
			j++;
		} else if (a[i] < b[j]) {
			cout << a[i] << " ";
			i++;
		} else {
			i++;
			j++;
		}
	}
	if (j == m) {
		while (i < n) {
			cout << a[i] << " ";
			i++;
		}
	}
	cout << endl;
	return 0;
}
