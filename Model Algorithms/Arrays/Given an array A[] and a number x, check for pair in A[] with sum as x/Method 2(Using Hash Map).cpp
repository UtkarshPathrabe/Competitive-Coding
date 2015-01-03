/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Using Hash Map to determine whether or not there exists two elements in array whose sum is exactly the given sum.
*/

/* Time Complexity: O(n) */
/* Auxiliary Space Complexity: O(R) where R is the range of integers. */

/* This method works in O(n) time if range of numbers is known. Let sum be the given sum and A[] be the array in which we need to find pair.
*	1) Initialize Binary Hash Map M[] = {false}
*	2) Do following for each element A[i] in A[]
*		(a)	If M[sum - A[i]] is set then print the pair (A[i], sum - A[i])
*		(b)	Set M[A[i]]
*/

#include <bits/stdc++.h>

using namespace std;

void printPairs (vector<int> &array, int n, int sum, int minimum) {
	vector<bool> binaryMap;
	vector<int> a;
	int addFactor;
	bool change = false;
	if (minimum < 0) {
		addFactor = abs(minimum);
		change = true;
	} else {
		addFactor = 0;
	}
	for (int i = 0; i < n; i++) {
		a.push_back(array[i] + addFactor);
	}
	sum += (2 * addFactor);
	for (int i = 0; i < (2 * sum); i++) {
		binaryMap.push_back(false);
	}
	for (int i = 0; i < n; i++) {
		int temp = sum - a[i];
		if ((temp >= 0) && (binaryMap[temp] == true)) {
			if (change) {
				cout << "Pair with given sum " << sum - (2 * addFactor) << " is (" << array[i] << ", " << temp - addFactor << ")." << endl;
			} else {
				cout << "Pair with given sum " << sum << " is (" << array[i] << ", " << temp << ")." << endl;
			}
		}
		binaryMap[a[i]] = true;
	}
	
}

int main (void) {
	int n, sum, ele, minimum = INT_MAX;
	cout << "Enter the number of elements in the array and enter them with a space between each of them. Also write the sum that you want to check for:" << endl;
	cin >> n;
	vector<int> array;
	for (int i = 0; i < n; i++) {
		cin >> ele;
		minimum = min(minimum, ele);
		array.push_back(ele);
	}
	cin >> sum;
	printPairs (array, n, sum, minimum);
	array.erase(array.begin(), array.end());
	return 0;
}
