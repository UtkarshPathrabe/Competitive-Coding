#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T;
	long long int maxi, K;
	cin >> T;
	while (T--) {
		maxi = -99999;
		cin >> K;
		for (int i = 1; i <= (K - i); i++) {
			maxi = max(maxi, i * (K - i));
		}
		cout << maxi << endl;
	}
	return 0;
}
