#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int Lx, Ly, Lz, x, y, z;
	double arr1[1000] = {0}, arr2[1000] = {0}, shortest = 9999999999;
	cin >> Lx >> Ly >> Lz >> x >> y >> z;
	if (x == 0) {
		cout << ((y*y) + (z*z)) << endl;
	} else if (y == 0) {
		cout << ((x*x) + (z*z)) << endl;
	} else if (z == 0) {
		cout << ((x*x) + (y*y)) << endl;
	} else {
		if (Lx == x) {
			for (int i = 0; i <= z; i++) {
				arr1[i] = sqrt((i*i) + (x*x));
				arr2[i] = sqrt(((z - i)*(z - i)) + (y*y));
				shortest = min((arr1[i] + arr2[i]) * (arr1[i] + arr2[i]), shortest);
			}
			for (int i = 0; i <= y; i++) {
				arr1[i] = sqrt((i*i) + (x*x));
				arr2[i] = sqrt(((y - i)*(y - i)) + (z*z));
				shortest = min((arr1[i] + arr2[i]) * (arr1[i] + arr2[i]), shortest);
			}
		} else if (Ly == y) {
			for (int i = 0; i <= z; i++) {
				arr1[i] = sqrt((i*i) + (y*y));
				arr2[i] = sqrt(((z - i)*(z - i)) + (x*x));
				shortest = min((arr1[i] + arr2[i]) * (arr1[i] + arr2[i]), shortest);
			}
			for (int i = 0; i <= x; i++) {
				arr1[i] = sqrt((i*i) + (z*z));
				arr2[i] = sqrt(((x - i) * (x - i)) + (y*y));
				shortest = min((arr1[i] + arr2[i]) * (arr1[i] + arr2[i]), shortest);
			}
		} else {
			for (int i = 0; i <= x; i++) {
				arr1[i] = sqrt((i*i) + (z*z));
				arr2[i] = sqrt(((x - i) * (x - i)) + (y*y));
				shortest = min((arr1[i] + arr2[i]) * (arr1[i] + arr2[i]), shortest);
			}
			for (int i = 0; i <= y; i++) {
				arr1[i] = sqrt((i*i) + (x*x));
				arr2[i] = sqrt(((y - i)*(y - i)) + (z*z));
				shortest = min((arr1[i] + arr2[i]) * (arr1[i] + arr2[i]), shortest);
			}
		}
		cout << (int)shortest << endl;
	}
	return 0;
}
