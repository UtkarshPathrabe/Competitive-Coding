#include <bits/stdc++.h>

using namespace std;

typedef long long int LLI;

LLI a[200005] = {0}, pre[200005] = {0}, suf[200005] = {0};

int main (void) {
	int n, k, x;
	cin >> n >> k >> x;
	LLI prod = 1, ans = 0;
	for (int i = 0; i < k; i++) {
		prod *= x;
	}
	for (int i = 1; i <= n; i++) {
		cin >> a[i];
		pre[i] = pre[i-1] | a[i];
	}
	for (int i = n; i > 0; i--) {
		suf[i] = suf[i+1] | a[i];
	}
	for (int i = 1; i <= n; i++) {
		ans = max (ans, (pre[i-1] | (a[i] * prod) | suf[i+1]));
	}
	cout << ans << endl;
	return 0;
}
