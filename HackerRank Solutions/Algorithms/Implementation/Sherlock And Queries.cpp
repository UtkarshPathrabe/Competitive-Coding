#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N, M;
	cin >> N >> M;
	long long int A[N], B[M], C[M];
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < M; i++) {
		cin >> B[i];
	}
	for (int i = 0; i < M; i++) {
		cin >> C[i];
	}
	for (int i = 1; i <= M; i++) {
		for (int j = 1; j <= N; j++) {
			if ((j % B[i - 1]) == 0) {
				A[j - 1] = A[j - 1] * C[i - 1];
			}
		}
	}
	for (int i = 0; i < N; i++) {
		cout << (A[i] % ((long long int)pow(10, 9) + 7)) << " ";
	}
	cout << endl;
	return 0;
}
