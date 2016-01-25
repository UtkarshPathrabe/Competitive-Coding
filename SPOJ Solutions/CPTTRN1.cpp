#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test, l, c;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> l >> c;
		for (int i = 0; i < l; i++) {
			for (int j = 0; j < c; j++) {
				if ((i+j)%2 == 0) {
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
