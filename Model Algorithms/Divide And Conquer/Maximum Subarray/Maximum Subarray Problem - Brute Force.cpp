/* Author : Utkarsh Ashok Pathrabe
*  Algorithm: Brute Force solution to solve Maximum Subarray Problem
*/

/* Time Complexity: O(n^2) */

#include <bits/stdc++.h>

using namespace std;

int Price[] = {100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97};
int Change[17];

int main (void) {
	int maxSum = INT_MIN, minIndex = -1, maxIndex = -1, sum;
	Change[0] = 0;
	for (int i = 1; i < 17; i++) {
		Change[i] = Price[i] - Price[i - 1];
	}
	for (int i = 0; i < 17; i++) {
		sum = 0;
		for (int j = i; j < 17; j++) {
			sum += Change[j];
			if (maxSum < sum) {
				maxSum = sum;
				minIndex = i;
				maxIndex = j;
			}
		}
	}
	sum = 0;
	cout << "The Maximum subarray is:" << endl;
	for (int k = minIndex; k <= maxIndex; k++) {
		cout << Price[k] << " ";
		sum += Price[k];
	}
	cout << endl << "The sum is: " << sum << endl;
	return 0;
}
