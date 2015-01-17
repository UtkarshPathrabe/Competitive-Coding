#include <bits/stdc++.h>

using namespace std;

long long int ValidPoints (long long int R) {
	long long int count = 0;
	for (long long int i = 1; i*i <= R; i++) {
		double integral;
		if (modf(sqrt(R - (i*i)), &integral) == 0.0) {
			count += 1;
		}
	}
	return (count * 4);
}

int main (void) {
	long long int t, r, k;
	cin >> t;
	while (t--) {
		cin >> r >> k;
		if (ValidPoints(r) <= k) {
			cout << "possible" << endl;
		} else {
			cout << "impossible" << endl;
		}
	}
	return 0;
}
