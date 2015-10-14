#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, a[2][50] = {0}, b[50] = {0};
	vector<int> sums;
	cin >> n;
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < n-1; j++) {
			cin >> a[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	for (int i = 0; i < n; i++) {
		int sum = b[i];
		for (int j = 0; j < n-1; j++) {
			if (j < i) {
				sum += a[0][j];
			} else {
				sum += a[1][j];
			}
		}
		sums.push_back(sum);
	}
	sort(sums.begin(), sums.end());
	cout << sums[0] + sums[1] << endl;
	return 0;
}
