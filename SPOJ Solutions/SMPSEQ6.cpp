#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, x;
	cin >> n >> x;
	int a[n+1], b[n+1];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	for (int i = 0; i < n; i++) {
		for (int y = -x; y <= x; y++) {
			if ((i+y >= 0) && (i+y < n) && (a[i] == b[i+y])) {
				cout << i+1 << " ";
				continue;
			}
		}
	}
	cout << endl;
	return 0;
}
