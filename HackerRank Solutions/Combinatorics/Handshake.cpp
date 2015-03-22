#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		cout << (N * (N - 1)) / 2 << endl;
	}
	return 0;
}
