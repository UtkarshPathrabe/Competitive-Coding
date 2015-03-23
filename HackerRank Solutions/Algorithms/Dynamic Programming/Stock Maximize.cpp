#include <bits/stdc++.h>

using namespace std;

long long int Profit (long long int price[], long long int N) {
	long long int Max[N], bestPrice = 0, stock = 0;
	memset (Max, 0, sizeof(Max));
	Max[N - 1] = price[N - 1];
	for (long long int i = N - 2; i >= 0; i--) {
		Max[i] = (price[i] > Max[i + 1]) ? price[i] : Max[i + 1];
	}
	for (long long int i = 0; i < N; i++) {
		if ((i == N - 1) || (Max[i + 1] < Max[i])) {
			bestPrice += stock * price[i];
			stock = 0;
		} else if (Max[i + 1] > price[i]) {
			stock++;
			bestPrice -= price[i];
		}
	}
	return bestPrice;
}

int main (void) {
	long long int T, N;
	cin >> T;
	while (T--) {
		cin >> N;
		long long int price[N];
		for (long long int i = 0; i < N; i++) {
			cin >> price[i];
		}
		cout << Profit (price, N) << endl;
	}
	return 0;
}
