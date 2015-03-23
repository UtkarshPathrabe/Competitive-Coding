#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		int x = -1, y = -1;
		for (int i = N/3; i >= 0; i--) {
			if (((N - (3 * i)) % 5) == 0) {
				x = i;
				y = (N - (3 * i)) / 5;
				break;
			}
		}
		if (x == -1) {
			cout << "-1" << endl;
		} else {
			for (int i = 0; i < 3 * x; i++) {
				cout << "5";
			}
			for (int i = 0; i < 5 * y; i++) {
				cout << "3";
			}
			cout << endl;
		}
	}
	return 0;
}
