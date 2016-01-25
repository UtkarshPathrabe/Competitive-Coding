#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test, n, x, y, a;
	cin >> test;
	while (test--) {
		cin >> n >> x >> y;
		a = x;
		while (a < n) {
			if (a % y != 0) {
				cout << a << " ";
			}
			a += x;
		}
		cout << endl;
	}
	return 0;
}
