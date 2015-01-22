#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, N, Num, Ans;
	unsigned long long int times;
	cin >> T;
	while (T--) {
		cin >> N;
		Ans = 0;
		for (int i = 0; i < N; i++) {
			cin >> Num;
			times = (unsigned long long int) (i + 1) * (N - i);
			if ((times % 2) == 1) {
				Ans ^= Num;
			}
		}
		cout << Ans << endl;
	}
	return 0;
}
