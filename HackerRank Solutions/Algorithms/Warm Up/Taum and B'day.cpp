#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T;
	cin >> T;
	while (T--) {
		long long int B, W, X, Y, Z;
		cin >> B >> W >> X >> Y >> Z;
		cout << min(X, Y + Z) * B + min(Y, X + Z) * W << endl;
	}
	return 0;
}
