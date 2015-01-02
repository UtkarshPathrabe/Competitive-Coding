/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Getting the nth Fibonacci Number using Memoization (Top Down)
*/

/* Memoization (Top Down): The memoized program for a problem is similar to the recursive program with a small modification that it looks into a lookup table before computing solutions.
*  First initialize the lookup array with all initial values as NIL. Whenever, we need a solution to a subproblem, we first look into the lookup table. If the precomputed value is there
*  then we return that value, otherwise we calculate the value and put the result in the lookup table so that it can be reused later. */

#include <bits/stdc++.h>
#define MAXLIMIT 100

using namespace std;

long long int fib[MAXLIMIT];

void Initialize () {
	for (int i = 0; i < MAXLIMIT; i++) {
		fib[i] = INT_MIN;
	}
}

long long int Fibonacci_Rec (int n) {
	if (fib[n] < 0) {
		if (n == 0) {
			fib[n] = 0;
		} else if (n == 1) {
			fib[n] = 1;
		} else {
			fib[n] = Fibonacci_Rec(n - 1) + Fibonacci_Rec(n - 2);
		}
	}
	return fib[n];
}

int main (void) {
	int n;
	char r;
	Initialize();
	do {
		cout << "Enter any positive number:" << endl;
		cin >>  n;
		cout << Fibonacci_Rec(n) << endl;
		cout << "Do you want to enter more numbers:(Press 'y' for 'yes')" << endl;
		cin >> r;
	}while (r == 'y');
	return 0;
}
