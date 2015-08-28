#include <bits/stdc++.h>

using namespace std;

int maxSumIS (int arr[], int n) {
	int *msis = (int*) calloc (n, sizeof(int));
	for (int i = 0; i < n; i++) {
		msis[i] = arr[i];
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if ((arr[i] > arr[j]) && (msis[i] < msis[j] + arr[i])) {
				msis[i] = msis[j] + arr[i];
			}
		}
	}
	int m = INT_MIN;
	for (int i = 0; i < n; i++) {
		m = max (m, msis[i]);
	}
	free(msis);
	return m;
}

int main (void) {
	int arr[] = {1, 101, 2, 3, 100, 4, 5};
	int n = sizeof (arr) / sizeof (arr[0]);
	cout << "Sum of maximum sum increasing subsequence is " << maxSumIS (arr, n) << "." << endl;
	return 0;
}
