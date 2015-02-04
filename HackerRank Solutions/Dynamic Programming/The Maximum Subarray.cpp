#include <bits/stdc++.h>

using namespace std;

int FindMaxCrossingSubarray (vector<int> &A, int low, int mid, int high, int * max_left, int * max_right) {
	int left_sum = INT_MIN, right_sum = INT_MIN, sum = 0;
	for (int i = mid; i >= low; i--) {
		sum = sum + A[i];
		if (left_sum < sum) {
			left_sum = sum;
			*max_left = i;
		}
	}
	sum = 0;
	for (int i = mid + 1; i <= high; i++) {
		sum = sum + A[i];
		if (right_sum < sum) {
			right_sum = sum;
			*max_right = i;
		}
	}
	return left_sum + right_sum;
}

int FindMaxSubarray (vector<int> &A, int low, int high, int * lowIndex, int * highIndex) {
	if (high == low) {
		*lowIndex = low;
		*highIndex = high;
		return A[low];
	} else {
		int mid = floor ((low + high) / 2), left_low, right_low, cross_low, left_high, right_high, cross_high, left_sum, right_sum, cross_sum;
		left_sum = FindMaxSubarray (A, low, mid, &left_low, &left_high);
		right_sum = FindMaxSubarray (A, mid + 1, high, &right_low, &right_high);
		cross_sum = FindMaxCrossingSubarray (A, low, mid, high, &cross_low, &cross_high);
		if ((left_sum > right_sum) && (left_sum > cross_sum)) {
			*lowIndex = left_low;
			*highIndex = left_high;
			return left_sum;
		} else if ((left_sum < right_sum) && (right_sum > cross_sum)) {
			*lowIndex = right_low;
			*highIndex = right_high;
			return right_sum;
		} else {
			*lowIndex = cross_low;
			*highIndex = cross_high;
			return cross_sum;
		}
	}
}

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		vector<int> A;
		int temp, unSum = 0, orSum = 0, m = INT_MIN, low, high;
		for (int i = 0; i < N; i++) {
			cin >> temp;
			A.push_back(temp);
			if (temp > 0) {
				unSum += temp;
			} else {
				m = max(m, temp);
			}
		}
		if (unSum == 0) {
			unSum = m;
		}
		orSum = FindMaxSubarray (A, 0, A.size() - 1, &low, &high);
		cout << orSum << " " << unSum << endl;
	}
	return 0;
}
