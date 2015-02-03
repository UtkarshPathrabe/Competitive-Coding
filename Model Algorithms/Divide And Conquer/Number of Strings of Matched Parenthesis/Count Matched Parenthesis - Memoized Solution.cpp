#include <bits/stdc++.h>

using namespace std;

int CountMatchedPairs (int k, int A[]) {
	if (k == 0) {
		A[k] = 1;
		return A[k];
	} else {
		int count = 0;
		for (int j = 1; j <= k; j++) {
			if (A[j - 1] == INT_MIN) 
				A[j - 1] = CountMatchedPairs (j - 1, A);
			if (A[k - j] == INT_MIN) 
				A[k - j] = CountMatchedPairs (k - j, A);
			count += A[j - 1] * A[k - j];
		}
		return count;
	}
}

int main (void) {
	int k;
	cout << "Enter the value of k:\t";
	cin >> k;
	int A[k+1];
	for (int i = 0; i <= k; i++) {
		A[i] = INT_MIN;
	}
	cout << "The number of strings of matched parenthesis of length " << 2*k << " is " << CountMatchedPairs (k, A) << endl;
	return 0;
}
