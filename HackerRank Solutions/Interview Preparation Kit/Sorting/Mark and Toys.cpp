#include <bits/stdc++.h>

using namespace std;

vector<long long int> price;

int main (void) {
	int N, count = 0;
	long long int K, temp;
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		price.push_back (temp);
	}
	sort (price.begin(), price.end());
	temp = 0;
	for (int i = 0; i < N; i++) {
		if (temp + price[i] <= K) {
			temp += price[i];
			count++;
		}
	}
	cout << count << endl;
	return 0;
}
