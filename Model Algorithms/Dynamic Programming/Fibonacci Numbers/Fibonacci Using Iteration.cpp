/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Getting the nth Fibonacci Number using Tabulation (Bottom Up)
*/

/* Tabulation (Bottom Up): The tabulated program for a given problem builds a table in the bottom up fashion and returns the last entry from table. */

#include <bits/stdc++.h>
#define MAXLIMIT 100

using namespace std;

long long int fib[MAXLIMIT];

void Initialize () {
	for (int i = 0; i < MAXLIMIT; i++) {
		fib[i] = INT_MIN;
	}
}

long long int Fibonacci_Ite (int n) {
	if (fib[n] < 0) {
		fib[0] = 0;
		fib[1] = 1;
		for (int i = 2; i <= n; i++) {
			fib[i] = fib[i - 1] + fib[i - 2];
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
		cout << Fibonacci_Ite (n) << endl;
		cout << "Do you want to enter more numbers:(Press 'y' for 'yes')" << endl;
		cin >> r;
	}while (r == 'y');
	return 0;
}
