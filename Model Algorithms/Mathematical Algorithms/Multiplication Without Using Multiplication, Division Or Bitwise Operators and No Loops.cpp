#include <bits/stdc++.h>

using namespace std;

int Multiply (int x, int y) {
	if (y == 0) {
		return 0;
	} else if (y > 0) {
		return (x + Multiply (x, y - 1));
	} else {
		return (-Multiply (x, -y));
	}
}

int main (void) {
	int x, y;
	cout << "Enter two integers to multiply:" << endl;
	cin >> x >> y;
	cout << "The Product is " << Multiply (x, y) << endl;
	return 0;
}
