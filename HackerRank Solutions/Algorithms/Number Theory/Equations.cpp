#include <bits/stdc++.h>
#define MAX 1000009
#define MOD 1000007

using namespace std;

int Prime[MAX] = {0}, Count[MAX] = {0};

void Initialize () {
	for (int i = 2; i <= MAX / i; i++) {
		if (!Prime[i]) {
			Prime[i] = i;
			for (int j = i * i; j < MAX; j += i) {
				Prime[j] = i;
			}
		}
	}
}

int main (void) {
	Initialize ();
	long long ans = 1;
	int N, M;
	cin >> N;
	for (int i = 2; i <= N; i++) {
		M = i;
		while (M > 1) {
			if (Prime[M] == 0) {
				Prime[M] = M;
			}
			Count[Prime[M]] += 2;
			M /= Prime[M];
		}
	}
	for (int i = 0; i <= N; i++) {
		ans = ans * (1 + Count[i]) % MOD;
	}
	cout << ans << endl;
	return 0;
}
