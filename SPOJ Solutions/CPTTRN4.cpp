#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test, l, c, h, w;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> l >> c >> h >> w;
		for (int i = 0; i < ((h+1)*l + 1); i++) {
			for (int j = 0; j < ((w+1)*c + 1); j++) {
				if ((i%(h+1) == 0) || (j%(w+1) == 0)) {
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
