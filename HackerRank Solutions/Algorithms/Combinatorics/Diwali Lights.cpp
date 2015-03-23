#include <bits/stdc++.h>

using namespace std;

int expo100000 (int x, int y) {
	int res = 1, temp = x;
	while (y) {
		if (y & 1) {
			res = (res * temp) % 100000;
		}
		temp = (temp * temp) % 100000;
		y >>= 1;
	}
	return res % 100000;
}

int main (void) {
	int T, N, ans;
	cin >> T;
	while (T--) {
		cin >> N;
		ans = expo100000 (2, N);
		ans--;
		if (ans == -1) ans = 99999;
		cout << ans << endl;
	}
	return 0;
}
