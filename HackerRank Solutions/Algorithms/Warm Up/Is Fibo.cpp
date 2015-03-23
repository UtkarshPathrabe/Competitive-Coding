#include <bits/stdc++.h>

using namespace std;

bool BSearch (long long int A[], int low, int high, long long int x) {
	if (low <= high) {
		int mid = (low + high) / 2;
		if (A[mid] == x) {
			return true;
		} else if (A[mid] > x) {
			return BSearch (A, low, mid - 1, x);
		} else {
			return BSearch (A, mid + 1, high, x);
		}
	}
	return false;
}

int main (void) {
	long long int Fib[60] = {0}, N;
	Fib[1] = 1; 
	for (int i = 2; i < 60; i++) {
		Fib[i] = Fib[i-1] + Fib[i-2];
	}
	int T;
	cin >> T;
	while (T--) {
		cin >> N;
		if (BSearch (Fib, 0, 59, N))
			cout << "IsFibo" << endl;
		else
			cout << "IsNotFibo" << endl;
	}
	return 0;
}
