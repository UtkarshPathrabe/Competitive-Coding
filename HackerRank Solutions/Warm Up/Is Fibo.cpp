#include <bits/stdc++.h>

using namespace std;

bool BSearch (unsigned long long int Fib[], int num, int start, int end) {
	if (start <= end) {
		int mid = (start + end) / 2;
		if (num == Fib[mid]) {
			return true;
		} else if (num > Fib[mid]) {
			return BSearch (Fib, num, mid + 1, end);
		} else if (num < Fib[mid]) {
			return BSearch (Fib, num, start, mid - 1);
		}
	}
	return false;
}

int main (void) {
	unsigned int T;
	unsigned long long int N, Fibonacci[60];
	Fibonacci[0] = 0;
	Fibonacci[1] = 1;
	for (int i = 2; i < 60; i++) {
		Fibonacci[i] = Fibonacci[i - 1] + Fibonacci[i - 2];
	}
	//ifstream cin("ABC.txt");
	//freopen ("Out.txt", "w", stdout);
	cin >> T;
	while (T--) {
		cin >> N;
		if (BSearch (Fibonacci, N, 0, 54)) {
			cout << "IsFibo" << endl;
		} else {
			cout << "IsNotFibo" << endl;
		}
	}
	return 0;
}
