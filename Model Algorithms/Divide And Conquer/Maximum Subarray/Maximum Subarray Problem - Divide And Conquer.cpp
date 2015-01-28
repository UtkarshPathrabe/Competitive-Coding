/* Author : Utkarsh Ashok Pathrabe
*  Algorithm: Divide and Conquer to solve Maximum Subarray Problem
*/

/* Time Complexity: O(n*log(n)) */

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
	int Price[] = {100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97}, maxSum, low, high, sum = 0;
	vector<int> Change;
	for (int i = 1; i < 17; i++) {
		Change.push_back (Price[i] - Price[i - 1]);
	}
	maxSum = FindMaxSubarray (Change, 0, Change.size() - 1, &low, &high);
	cout << "The Maximum subarray is:" << endl;
	for (int k = low + 1; k <= high + 1; k++) {
		cout << Price[k] << " ";
		sum += Price[k];
	}
	cout << endl << "The sum is: " << sum << endl;
	return 0;
}
