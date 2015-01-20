#include <bits/stdc++.h>

using namespace std;

int Traingle (long long int n) {
	if ((n == 1) || (n == 2)) {
		return -1;
	} else if (n % 2 == 1) {
		return 2;
	} else {
		if (n % 4 == 0) {
			return 3;
		} else {
			return 4;
		}
	}
}

int main (void) {
	int test;
	cin >> test;
	while (test--) {
		long long int N;
		cin >> N;
		cout << Traingle(N) << endl;
	}
	return 0;
}
