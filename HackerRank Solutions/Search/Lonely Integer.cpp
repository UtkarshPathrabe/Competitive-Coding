#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, ans = 0, temp;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		ans ^= temp;
	}
	cout << ans << endl;
	return 0;
}
