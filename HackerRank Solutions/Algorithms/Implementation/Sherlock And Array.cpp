#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		int A[N], leftSum = 0, rightSum = 0, flag = 0;
		for (int i = 0; i < N; i++) {
			cin >> A[i];
			rightSum += A[i];
		}
		rightSum -= A[0];
		if (N == 1) {
			cout << "YES" << endl;
			flag = 1;
		} else {
			for (int i = 1; i < N; i++) {
				leftSum += A[i-1];
				rightSum -= A[i];
				if (leftSum == rightSum) {
					cout << "YES" << endl;
					flag = 1;
					break;
				}
			}
		}
		if (flag == 0) {
			cout << "NO" << endl;
		}
	}
	return 0;
}
