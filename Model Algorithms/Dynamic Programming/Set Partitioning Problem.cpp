/* Time Complexity: O(sum*n); Space Complexity: O(sum*n) */

#include <bits/stdc++.h>

using namespace std;

bool findPartition (vector<int> &arr) {
	int sum = 0, n = arr.size();
	for (int i = 0; i < n; i++) {
		sum += arr[i];
	}
	if (sum%2 != 0) {
		return false;
	}
	bool flag[sum/2 + 1][n + 1];
	for (int i = 0; i <= n; i++) {
		flag[0][i] = true;
	}
	for (int j = 1; j <= (sum/2); j++) {
		flag[j][0] = false;
	}
	for (int i = 1; i <= (sum/2); i++) {
		for (int j = 1; j <= n; j++) {
			flag[i][j] = flag[i][j-1];
			if (i >= arr[j-1]) {
				flag[i][j] = flag[i][j] || flag[i-arr[j-1]][j-1];
			}
		}
	}
	return flag[(sum/2)][n];
}

int main (void) {
	int arr[] = {3, 1, 1, 2, 2, 1};
	int n = sizeof(arr)/sizeof(arr[0]);
	vector<int> set(arr, arr+n);
	if (findPartition(set) == true)
		cout << "Given set can be divided into two subsets of equal sum." << endl;
	else
		cout << "Given set cannot be divided into two subsets of equal sum." << endl;
	return 0;
}
