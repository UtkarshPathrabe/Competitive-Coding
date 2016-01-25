#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int a, b, sum = 0;
	cin >> a >> b;
	for (int i = a; i <= b; i++) {
		sum += (i*i);
	}
	cout << sum << endl;
	return 0;
}
