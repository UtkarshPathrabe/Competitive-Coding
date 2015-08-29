/* Time Complexity: O(log(n)); Space Complexity: O(1)[O(log(n)), if function call stack size is considered.] */

#include <bits/stdc++.h>
#define LLI long long int

using namespace std;

void multiply (LLI F[2][2], LLI M[2][2]) {
	LLI w = F[0][0]*M[0][0] + F[0][1]*M[1][0];
	LLI x = F[0][0]*M[0][1] + F[0][1]*M[1][1];
	LLI y = F[1][0]*M[0][0] + F[1][1]*M[1][0];
	LLI z = F[1][0]*M[0][1] + F[1][1]*M[1][0];
	F[0][0] = w;
	F[0][1] = x;
	F[1][0] = y;
	F[1][1] = z;
}

void power (LLI F[2][2], int n) {
	if ((n == 0) || (n == 1)) {
		return;
	}
	power (F, n/2);
	multiply (F, F);
	if (n % 2 != 0) {
		LLI M[2][2] = {{1, 1}, {1, 0}};
		multiply (F, M);
	}
}

LLI fib (int n) {
	if (n <= 0) {
		return 0;
	} else if (n == 1) {
		return 1;
	} else {
		LLI F[2][2] = {{1, 1}, {1, 0}};
		power (F, n-1);
		return F[0][0];
	}
}

int main (void) {
	int n = 10;
	cout << "Fibonacci of " << n << " is " << fib(n) << "." << endl;
	return 0;
}
