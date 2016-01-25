#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test, l, c;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> l >> c;
		for (int i = 0; i < l; i++) {
			for (int j = 0; j < c; j++) {
				if ((i == 0) || (i == l-1) || (j == 0) || (j == c-1)) {
					cout << "*";
				} else {
					cout << ".";
				}
			}
			cout << endl;
		}
		cout << endl;
	}
	return 0;
}
