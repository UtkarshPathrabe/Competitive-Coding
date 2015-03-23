#include <bits/stdc++.h>

using namespace std;

int LinearSearch (int A[], int len, int num, int exclude) {
	for (int i = 0; i < len; i++) {
		if ((i != exclude) && (A[i] == num)) {
			return i;
		}
	}
	return -1;
}

int main (void) {
	int T, M, N, temp;
	cin >> T;
	while (T--) {
		cin >> M >> N;
		int A[N];
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}
		for (int i = 0; i < N; i++) {
			temp = LinearSearch(A, N, M - A[i], i);
			if (temp != -1) {
				cout << min (i + 1, temp + 1) << " " << max (i + 1, temp + 1) << endl;
				break;
			}
		}
	}
	return 0;
}
