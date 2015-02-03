#include <bits/stdc++.h>

using namespace std;

int CountMatchedPairs (int k) {
	if (k == 0) {
		return 1;
	} else {
		int count = 0;
		for (int j = 1; j <= k; j++) {
			count += CountMatchedPairs (j - 1) * CountMatchedPairs (k - j);
		}
		return count;
	}
}

int main (void) {
	int k;
	cout << "Enter the value of k:\t";
	cin >> k;
	cout << "The number of strings of matched parenthesis of length " << 2*k << " is " << CountMatchedPairs (k) << endl;
	return 0;
}
