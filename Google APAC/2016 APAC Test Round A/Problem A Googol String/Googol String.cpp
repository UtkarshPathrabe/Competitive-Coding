#include <bits/stdc++.h>

using namespace std;

long long int len[65] = {0};

int solve (long long int K) {
	int i;
	for (i = 0; i < 65; i++) {
		if (len[i] >= K) {
			break;
		}
	}
	if (len[i-1]+1 == K) {
		return 0;
	}
	return ((solve(len[i]-K+1))^1);
}

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("A-large-practice.out");
	cin.open("A-large-practice.in");
	int T;
	cin >> T;
	for (int i = 1; i < 65; i++) {
		len[i] = (2 * len[i-1]) + 1;
	}
	for (int t = 1; t <= T; t++) {
		long long int K;
		cin >> K;
		cout << "Case #" << t << ": " << solve(K) << endl;
	}
	cout.close();
	cin.close();
	return 0;
}
