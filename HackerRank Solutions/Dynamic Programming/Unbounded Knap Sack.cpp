#include <bits/stdc++.h>

using namespace std;

int UnboundedKnapSack (int value[], int n, int k) {
	int Max[k + 1], temp;
	for (int i = 0; i <= k; i++) {
		Max[i] = 0;
	}
	for (int i = 1; i <= k; i++) {
		Max[i] = Max[i - 1];
		for (int j = 0; j < n; j++) {
			if (i >= value[j]) {
				temp = Max[i - value[j]] + value[j];
			}
			if (temp > Max[i]) {
				Max[i] = temp;
			}
		}
	}
	return Max[k];
}

int main (void) {
	int T, n, k;
	cin >> T;
	while (T--) {
		cin >> n >> k;
		int value[n];
		for (int i = 0; i < n; i++) {
			cin >> value[i];
		}
		cout << UnboundedKnapSack (value, n, k) << endl;
	}
	return 0;
}
