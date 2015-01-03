/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Using sorting to determine whether or not there exists two elements in array whose sum is exactly the given sum.
*/

/* Time Complexity: Depends on sorting algorithm. Here O(n^2) in worst case for quick sort, O(n*log(n)) in average case.  */
/* Auxiliary Space Complexity: Depends on sorting algorithm. Here O(1) */

/* Algorithm:
*	hasArrayTwoCandidates (A[], ar_size, sum)
*	1) Sort the array in non-decreasing order.
*	2) Initialize two index variables to find the candidate elements in the sorted array.
*		(a) Initialize first to the leftmost index: l = 0
*		(b) Initialize second  the rightmost index:  r = ar_size-1
*	3) Loop while l < r.
*		(a) If (A[l] + A[r] == sum)  then return 1
*		(b) Else if( A[l] + A[r] <  sum )  then l++
*		(c) Else r--    
*	4) No candidates in whole array - return 0
*/

/* Note: If there are more than one pair having the given sum then this algorithm reports only one. */

#include <bits/stdc++.h>

using namespace std;

void swap (int * a, int * b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition (vector<int> &array, int start, int end) {
	int i = start - 1, j, x = array[end];
	for (j = start; j < end; j++) {
		if (array[j] < x) {
			swap(&array[++i], &array[j]);
		}
	}
	swap(&array[++i], &array[end]);
	return i;
}

void quickSort (vector<int> &array, int start, int end) {
	if (start < end) {
		int mid = partition(array, start, end);
		quickSort(array, start, mid - 1);
		quickSort(array, mid + 1, end);
	}
}

bool hasArrayTwoCandidates (vector<int> &array, int n, int sum) {
	quickSort (array, 0, n - 1);
	int left = 0, right = n - 1;
	while (left < right) {
		if (array[left] + array[right] == sum) {
			return true;
		} else if (array[left] + array[right] < sum) {
			left += 1;
		} else {
			right -= 1;
		}
	}
	return false;
}

int main (void) {
	int n, sum, ele;
	cout << "Enter the number of elements in the array and enter them with a space between each of them. Also write the sum that you want to check for:" << endl;
	cin >> n;
	vector<int> array;
	for (int i = 0; i < n; i++) {
		cin >> ele;
		array.push_back(ele);
	}
	cin >> sum;
	if (hasArrayTwoCandidates (array, n, sum)) {
		cout << "Array has two elements with sum " << sum << "." << endl;
	} else {
		cout << "Array doesn't have two elements with sum " << sum << "." << endl;
	}
	array.erase(array.begin(), array.end());
	return 0;
}
