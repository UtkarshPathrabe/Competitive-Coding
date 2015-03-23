#include <bits/stdc++.h>

using namespace std;

int Arr[200002] = {0};

void Merge (int start, int mid, int end) {
	int A1[mid + 1 - start], A2[end - mid];
	for (int i = start, j = 0; i <= mid; i++, j++) {
		A1[j] = Arr[i];
	}
	for (int i = mid + 1, j = 0; i <= end; i++, j++) {
		A2[j] = Arr[i];
	}
	int i = 0, j = 0, k = start;
	while ((i < (mid + 1 - start)) && (j < (end - mid))) {
		if (A1[i] < A2[j]) {
			Arr[k++] = A1[i++];
		} else {
			Arr[k++] = A2[j++];
		}
	}
	while (i != (mid + 1 - start)) {
		Arr[k++] = A1[i++];
	}
	while (j != (end - mid)) {
		Arr[k++] = A2[j++];
	}
}

void MergeSort (int start, int end) {
	if (start < end) {
		int mid = (start + end) / 2;
		MergeSort (start, mid);
		MergeSort (mid + 1, end);
		Merge (start, mid, end);
	}
}

int main (void) {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> Arr[i];
	}
	MergeSort (0, n - 1);
	int Diff[n - 1], mi = INT_MAX;
	for (int i = 0; i < n - 1; i++) {
		Diff[i] = Arr[i + 1] - Arr[i];
		mi = min (mi, Diff[i]);
	}
	for (int i = 0; i < n - 1; i++) {
		if (mi == Diff[i]) {
			cout << Arr[i] << " " << Arr[i + 1] << " ";
		}
	}
	cout << endl;
	return 0;
}
