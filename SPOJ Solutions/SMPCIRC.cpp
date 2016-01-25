#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test;
	double x1, x2, y1, y2, r1, r2, dist;
	cin >> test;
	while (test--) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		dist = sqrt (pow (x2 - x1, 2) + pow (y2 - y1, 2));
		if ((dist == abs (r1 + r2)) || (dist == abs (r1 - r2))) {
			cout << "E" << endl;
		} else if (dist < abs (r1 - r2)) {
			cout << "I" << endl;
		} else {
			cout << "O" << endl;
		}
	}
	return 0;
}
