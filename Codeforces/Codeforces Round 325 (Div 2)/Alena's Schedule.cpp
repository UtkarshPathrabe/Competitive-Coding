#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, state = 0, a, count = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		switch (state) {
			case 0:
				if (a == 1) {
					count++;
					state = 1;
				}
				break;
			case 1:
				if (a == 1) {
					count++;
				} else {
					count++;
					state = 2;
				}
				break;
			case 2:
				if (a == 1) {
					count++;
					state = 1;
				} else {
					count--;
					state = 0;
				}
				break;
		}
	}
	if (state == 2) {
		cout << count - 1 << endl;
	} else {
		cout << count << endl;
	}
	return 0;
}
