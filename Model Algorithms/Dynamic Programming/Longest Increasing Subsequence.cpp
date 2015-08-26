/*
Time Complexity: O(n^2)
*/

#include <bits/stdc++.h>

using namespace std;

int LIS (vector<int> &arr) {
	int max = INT_MIN, n = arr.size();
	vector<int> lis;
	for (int i = 0; i < n; i++) {
		lis.push_back(1);
	}
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if ((arr[i] > arr[j]) && (lis[i] < lis[j] + 1)) {
				lis[i] = lis[j] + 1;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		if (max < lis[i]) {
			max = lis[i];
		}
	}
	lis.erase(lis.begin(), lis.end());
	return max;
}

int main (void) {
	vector<int> arr;
	arr.push_back (10);
	arr.push_back (22);
	arr.push_back (9);
	arr.push_back (33);
	arr.push_back (21);
	arr.push_back (50);
	arr.push_back (41);
	arr.push_back (60);
	arr.push_back (80);
	cout << "Length of Longest Increasing Subsequence is " << LIS(arr) << "." << endl;
	return 0;
}
