#include <bits/stdc++.h>
#define LLI long long int

using namespace std;

int main (void) {
	LLI a, b;
	cin >> a >> b;
	if (b > a) {
		cout << "-1" << endl;
	} else if (b == a) {
		cout << a << endl;
	} else {
		double u, v;
		LLI x, y;
		u = (a + b) / 2.0;
		v = (a - b) / 2.0;
		x = (a + b) / (2 * b);
		y = (a - b) / (2 * b);
		u = u / (double)x;
		v = v / (double)y;
		printf ("%.12lf\n", min (u, v));
	}
	return 0;
}
