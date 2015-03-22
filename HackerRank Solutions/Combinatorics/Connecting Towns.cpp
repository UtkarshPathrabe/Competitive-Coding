#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		long long int temp, ans = 1;
		cin >> N;
		for (int i = 0; i < N - 1; i++) {
			cin >> temp;
			ans = (ans * temp) % 1234567;
		}
		cout << ans % 1234567 << endl;
	}
	return 0;
}
