#include <bits/stdc++.h>

using namespace std;

int main (void) {
	double a, sum = 0;
	for (int i = 0; i < 12; i++) {
		scanf ("%lf", &a);
		sum += a;
	}
	cout << (sum / 12.0) << endl;
	return 0;
}
