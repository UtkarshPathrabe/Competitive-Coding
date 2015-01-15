#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int L, R, maxi = INT_MIN;
	cin >> L >> R;
	for (int i = L; i <= R; i++) {
		for (int j = L; j <= R; j++) {
			maxi = max(maxi, i^j);
		}
	}
	cout << maxi << endl;
	return 0;
}
