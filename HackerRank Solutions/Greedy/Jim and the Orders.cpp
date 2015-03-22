#include <bits/stdc++.h>

using namespace std;

vector< pair<int, int> > custQueue;

bool myComparator (pair<int, int> x, pair<int, int> y) {
	if (x.second == y.second)
		return x.first < y.first;
	else
		return x.second < y.second;
}

int main (void) {
	int n, d, t;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> t >> d;
		custQueue.push_back(make_pair(i, t+d));
	}
	sort (custQueue.begin(), custQueue.end(), myComparator);
	for (int i = 0; i < n; i++) {
		cout << custQueue[i].first << " ";
	}
	cout << endl;
	return 0;
}
