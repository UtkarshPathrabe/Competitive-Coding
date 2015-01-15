#include <bits/stdc++.h>

using namespace std;

int lane[100005] = {0};

int FindMin (int start, int end) {
	int m = 3;
	for (int i = start; i <= end; i++) {
		m = min (m, lane[i]);
	}
	return m;
}

int main (void) {
	int N, T, i, j;
	cin >> N >> T;
	for (int i = 0; i < N; i++) {
		cin >> lane[i];
	}
	while (T--) {
		cin >> i >> j;
		cout << FindMin (i, j) << endl;
	}
	return 0;
}
