/* Time Complexity: O(n); Space Complexity: O(1) */

#include <bits/stdc++.h>
#define LLI long long int

using namespace std;

LLI fib (int n) {
	LLI a = 0, b = 1, c;
	for (int i = 2; i <= n; i++) {
		c = a + b;
		a = b;
		b = c;
	}
	return b;
}

int main (void) {
	int n = 10;
	cout << "Fibonacci of " << n << " is " << fib(n) << "." << endl;
	return 0;
}
