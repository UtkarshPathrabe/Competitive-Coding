#include <bits/stdc++.h>

using namespace std;

bool myComparatorX (const pair<unsigned long long int, int> &x, const pair<unsigned long long int, int> &y) {
	if (x.first == y.first)
		return x.second < y.second;
	else
		return x.first > y.first;
}

bool myComparatorY (const pair<unsigned long long int, int> &x, const pair<unsigned long long int, int> &y) {
	if (x.first == y.first)
		return x.second > y.second;
	else
		return x.first > y.first;
}

int main (void) {
	int T;
	cin >> T;
	while (T--) {
		int M, N, len, xCut = 1, yCut = 1;
		unsigned long long int temp, cutCost = 0;
		vector < pair <unsigned long long int, int> > cutPrice;
		cin >> M >> N;
		for (int i = 0; i < M - 1; i++) {
			cin >> temp;
			cutPrice.push_back (make_pair (temp, 1));
		}
		for (int i = 0; i < N - 1; i++) {
			cin >> temp;
			cutPrice.push_back (make_pair (temp, 2));
		}
		len = cutPrice.size ();
		if (M >= N)
			sort (cutPrice.begin (), cutPrice.end (), myComparatorX);
		else
			sort (cutPrice.begin (), cutPrice.end (), myComparatorY);
		for (int i = 0; i < len; i++) {
			if (cutPrice[i].second == 1) {
				xCut++;
				cutCost = (cutCost + (yCut * cutPrice[i].first) % 1000000007) % 1000000007;
			} else {
				yCut++;
				cutCost = (cutCost + (xCut * cutPrice[i].first) % 1000000007) % 1000000007;
			}
		}
		cout << cutCost % 1000000007 << endl;
	}
	return 0;
}
