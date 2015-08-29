#include <bits/stdc++.h>

using namespace std;

int minJumps (int arr[], int n) {
	int *jumps = (int*) calloc (n, sizeof(int));
	if ((n == 0) || (arr[0] == 0)) {
		return INT_MAX;
	}
	jumps[0] = 0;
	for (int i = 1; i < n; i++) {
		jumps[i] = INT_MAX;
		for (int j = 0; j < i; j++) {
			if ((i <= j + arr[j]) && (jumps[j] != INT_MAX)) {
				jumps[i] = min (jumps[i], jumps[j] + 1);
			}
		}
	}
	return jumps[n-1];
}

int main (void) {
	int arr[] = {1, 3, 6, 1, 0, 9};
	int size = sizeof (arr) / sizeof (arr[0]);
	cout << "Minimum number of jumps to reach end is " << minJumps (arr, size) << "." << endl;
	return 0;
}
