#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N, K, Q, temp;
	cin >> N >> K >> Q;
	int A[N];
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < Q; i++) {
		cin >> temp;
		cout << A[(N - (K % N) + temp) % N] << endl;
	}
	return 0;
}
