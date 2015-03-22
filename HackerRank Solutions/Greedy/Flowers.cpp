#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N, K, temp, amount = 0;
	vector<int> price;
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		price.push_back (temp);
	}
	sort (price.rbegin(), price.rend());
	for (int i = 0; i < N; i++) {
		amount += (((i/K) + 1) * price[i]);
	}
	cout << amount << endl;
	return 0;
}
