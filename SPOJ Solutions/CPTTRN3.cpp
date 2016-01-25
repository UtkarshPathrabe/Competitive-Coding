#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test, l, c;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> l >> c;
		for (int i = 0; i < (3*l + 1); i++) {
			for (int j = 0; j < (3*c + 1); j++) {
				if ((i%3 == 0) || (j %3 == 0)) {
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
