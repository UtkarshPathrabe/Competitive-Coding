#include <bits/stdc++.h>

using namespace std;

int main (void) {
	unsigned int T, num;
	cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		cin >> num;
		cout << ~num << endl;
	}
	return 0;
}
