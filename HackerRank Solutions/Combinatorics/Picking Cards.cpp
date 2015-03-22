#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T;
	cin >> T;
	while (T--) {
		int N, c;
		long long int ans = 1;
		cin >> N;
		int count[N];
		for (int i = 0; i < N; i++)
			count[i] = 0;
		for (int i = 0; i < N; i++) {
			cin >> c;
			count[c] += 1;
		}
		for (int i = 1; i < N; i++) {
			count[i] += count[i-1];
		}
		for (int i = 0; i < N; i++) {
			ans = ans * (count[i] - i) % 1000000007;
			if (count[i] < i) {
				break;
			}
		}
		cout << ans << endl;
	}
	return 0;
}
