#include <bits/stdc++.h>

using namespace std;

int GCD (int a, int b) {
	while (b) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int main (void) {
	int T, N;
	bool flag;
	cin >> T;
	while (T--) {
		flag = false;
		cin >> N;
		int A[N];
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}
		for (int i = 0; i < N; i++) {
			set<int> S;
			set<int> :: iterator it;
			S.insert(A[i]);
			for (int j = i; j < N; j++) {
				S.insert(A[j]);
				int gcd = A[j];
				for (it = S.begin(); it != S.end(); it++) {
					gcd = GCD(gcd, *it);
				}
				if (gcd == 1) {
					flag = true;
					break;
				}
			}
			if (flag) {
				break;
			}
			S.erase(S.begin(), S.end());
		}
		if (flag) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
	return 0;
}
