/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Mathematical Algorithms */

#include <bits/stdc++.h>

using namespace std;

long long int MultiplyBySeven (long long int number) {
	return ((number << 3) - number);
}

int main (void) {
	long long int n;
	cout << "Enter any number:" << endl;
	cin >> n;
	cout << n << " * 7 = " << MultiplyBySeven (n) << endl;
	return 0;
}
