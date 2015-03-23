#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T;
	cin >> T;
	while (T--) {
		int N, K, temp, count = 0;
		cin >> N >> K;
		for (int i = 0; i < N; i++) {
			cin >> temp;
			if (temp <= 0)
				count++;
		}
		if (count < K)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
