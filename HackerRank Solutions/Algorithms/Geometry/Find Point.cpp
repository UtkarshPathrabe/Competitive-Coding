#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, Px, Py, Qx, Qy;
	cin >> T;
	while (T--) {
		cin >> Px >> Py >> Qx >> Qy;
		cout << (2 * Qx) - Px << " " << (2 * Qy) - Py << endl;
	}
	return 0;
}
