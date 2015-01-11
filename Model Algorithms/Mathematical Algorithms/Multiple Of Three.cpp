/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Mathematical Algorithms */

#include <bits/stdc++.h>

using namespace std;

bool IsMultipleOfThree (long long int number) {
	if (number < 0)
		number = -number;
	if (number == 0)
		return 1;
	if (number == 1)
		return 0;
	int OddCount = 0, EvenCount = 0;
	while (number) {
		if (number & 1) {
			OddCount++;
		}
		if (number & 2) {
			EvenCount++;
		}
		number = number >> 2;
	}
	return IsMultipleOfThree (abs (OddCount - EvenCount));
}

int main (void) {
	long long int n;
	cout << "Enter any number:" << endl;
	cin >> n;
	if (IsMultipleOfThree (n)) {
		cout << n << " is a multiple of 3." << endl;
	} else {
		cout << n << " is not a multiple of 3." << endl;
	}
	return 0;
}
