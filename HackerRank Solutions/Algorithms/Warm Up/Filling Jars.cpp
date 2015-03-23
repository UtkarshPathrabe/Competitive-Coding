#include <bits/stdc++.h>

using namespace std;

int main (void) {
	long long int N, M, a, b, k, sum = 0;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> k;
		sum += (b - a + 1)*k;
	}
	cout << sum/N << endl;
	return 0;
}
