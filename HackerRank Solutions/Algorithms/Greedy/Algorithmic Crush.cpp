#include <bits/stdc++.h>

using namespace std;

vector< pair < int, pair < int, int> > > algo;

int main (void) {
	int N, M, a, b, k, size;
	long long int maxi = 0, temp = 0;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		cin >> a >> b >> k;
		algo.push_back (make_pair (a, make_pair (-1, k)));
		algo.push_back (make_pair (b, make_pair (1, k)));
	}
	sort (algo.begin (), algo.end ());
	size = algo.size ();
	for (int i = 0; i < size; i++) {
		if (algo[i].second.first == -1)
			temp += algo[i].second.second;
		else
			temp -= algo[i].second.second;
		maxi = max (maxi, temp);
	}
	cout << maxi << endl;
	return 0;
}
