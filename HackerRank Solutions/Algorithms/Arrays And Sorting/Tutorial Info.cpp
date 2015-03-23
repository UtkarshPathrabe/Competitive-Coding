#include <bits/stdc++.h>

using namespace std;

int BSearch (int ar[], int num, int start, int end) {
	if (start <= end) {
		int mid = (start + end) / 2;
		if (num == ar[mid]) {
			return mid;
		} else if (num > ar[mid]) {
			return BSearch (ar, num, mid + 1, end);
		} else {
			return BSearch (ar, num, start, mid - 1);
		}
	}
	return -1;
}

int main (void) {
	int V, n;
	cin >> V >> n;
	int ar[n];
	for (int i = 0; i < n; i++) {
		cin >> ar[i];
	}
	cout << BSearch (ar, V, 0, n - 1) << endl;
	return 0;
}
