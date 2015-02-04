#include <bits/stdc++.h>

using namespace std;

int main (void) {
	long long int N, K, val, ans = 0;
	set<long long int> Set;
	set<long long int>::iterator it;
	cin >> N >> K;
	for (long long int i = 0; i < N; i++) {
		cin >> val;
		Set.insert (val);
	}
	for (it = Set.begin(); it != Set.end(); it++) {
		if (Set.find((*it) + K) != Set.end()) {
			ans += 1;
		}
	}
	cout << ans << endl;
	return 0;
}
