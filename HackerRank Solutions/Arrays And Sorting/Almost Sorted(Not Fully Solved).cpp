#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n;
	cin >> n;
	int D[n], deform[5], j = 0, flag = 1;
	for (int i = 0; i < 5; i++) {
		deform[i] = -1;
	}
	cin >> D[0];
	for (int i = 1; i < n; i++) {
		cin >> D[i];
		if ((D[i - 1] > D[i]) && (flag)) {
			deform[min(j++, 4)] = i - 1;
			flag = 0;
		}
		if ((D[i - 1] < D[i]) && (!flag)) {
			deform[min(j++, 4)] = i - 1;
			flag = 1;
		}
	}
	if (deform[4] != -1) {
		cout << "no" << endl;
	} else {
		cout << "yes" << endl;
		if ((deform[2] == -1) && (deform[3] == -1)) {
			cout << "reverse " << deform[0] + 1 << " " << deform[1] + 1 << endl;
		} else {
			cout << "swap " << deform[0] + 1 << " " << deform[3] + 1 << endl;
		}
	}
	return 0;
}
