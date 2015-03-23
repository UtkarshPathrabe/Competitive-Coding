#include <bits/stdc++.h>

using namespace std;

vector<long long int> A, B;

int main (void) {
	int T;
	cin >> T;
	while (T--) {
		int N;
		long long int K, temp;
		bool flag = true;
		cin >> N >> K;
		for (int i = 0; i < N; i++) {
			cin >> temp;
			A.push_back (temp);
		}
		for (int i = 0; i < N; i++) {
			cin >> temp;
			B.push_back (temp);
		}
		sort (A.begin(), A.end());
		sort (B.rbegin(), B.rend());
		for (int i = 0; i < N; i++) {
			if (A[i] + B[i] < K) {
				flag = false;
				break;
			}
		}
		if (flag)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
		A.erase(A.begin(), A.end());
		B.erase(B.begin(), B.end());
	}
	return 0;
}
