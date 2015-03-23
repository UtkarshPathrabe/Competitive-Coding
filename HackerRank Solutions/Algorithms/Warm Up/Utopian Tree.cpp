#include <bits/stdc++.h>

using namespace std;

int height (int N) {
	int h = 1;
	for (int i = 1; i <= N; i++) {
		if ((i % 2) == 1) {
			h *= 2;
		} else {
			h += 1;
		}
	}
	return h;
}

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		cout << height(N) << endl;
	}
	return 0;
}
