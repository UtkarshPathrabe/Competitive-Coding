#include <bits/stdc++.h>

using namespace std;

long long int Count[1000002] = {0};

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		long long int A[N], count = 0;
		for (int i = 0; i < 1000002; i++)
			Count[i] = 0;
		for (int i = 0; i < N; i++) {
			cin >> A[i];
			Count[A[i]] += 1;
		}
		for (int i = 0; i < 1000002; i++) {
			count += (Count[i] * (Count[i] - 1));
		}
		cout << count << endl;
	}
	return 0;
}
