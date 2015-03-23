#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, A, B, sum;
	cin >> T;
	while (T--) {
		cin >> A >> B;
		cout << (int)sqrt(B) - (int)sqrt(A - 1) << endl;
	}
	return 0;
}
