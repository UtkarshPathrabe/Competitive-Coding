/* Time Complexity: O(n^2); Space Complexity: O(n) */

#include <bits/stdc++.h>

using namespace std;

int cutRod (int price[], int n) {
	int* val = (int*) calloc (n+1, sizeof(int));
	for (int i = 1; i <= n; i++) {
		int max_val = INT_MIN;
		for (int j = 0; j < i; j++) {
			max_val = max (max_val, price[j] + val[i-j-1]);
		}
		val[i] = max_val;
	}
	return val[n];
}

int main (void) {
	int price[] = {1, 5, 8, 9, 10, 17, 17, 20};
	int size = sizeof (price) / sizeof (price[0]);
	cout << "Maximum Obtainable Value is " << cutRod (price, size)  << "." << endl;
	return 0;
}
