#include <bits/stdc++.h>

using namespace std;

int main (void) {
	unsigned long long int total = 0, N, a, b, x = INT_MAX, y = INT_MAX;
	freopen ("Input.txt", "r", stdin);
	freopen ("Output.txt", "w", stdout);
	cin >> N;
	while (N--) {
		cin >> a >> b;
		x = min (x, a);
		y = min (y, b);
	}
	total = x * y;
	cout << total << endl;
	return 0;
}
