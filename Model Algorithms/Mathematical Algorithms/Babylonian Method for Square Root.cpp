/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Mathematical Algorithms
*/

#include <bits/stdc++.h>

using namespace std;

float SquareRoot (float Number) {
	float x = Number, y = 1.0, error = 0.000001;
	while ((x - y) > error) {
		x = (x + y) / 2;
		y = Number / x;
	}
	return x;
}

int main (void) {
	float n;
	cout << "Enter any positive integer: " << endl;
	cin >> n;
	cout << "The Square Root of " << n << " is " << SquareRoot(n) << endl;
	return 0;
}
