#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N, K;
	cin >> N >> K;
	long long int candies[N], unfair = INT_MAX;
	for (int i = 0; i < N; i++) {
		cin >> candies[i];
	}
	sort (candies, candies + N);
	for (int k = K - 1, i = 0; k < N; k++, i++) {
		unfair = min (unfair, candies[k] - candies[i]);
	}
	cout << unfair << endl;
	return 0;
}
