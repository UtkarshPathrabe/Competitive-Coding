#include <bits/stdc++.h>
#define zero(n) memset(n, 0, sizeof(n))

using namespace std;

int CountAllChildren (vector<int> *v, int *c, int offset) {
	int t = 0;
	if (v[offset].size() == 0) {
		c[offset] = 1;
	} else if (0 == c[offset]) {
		for (int i = 0; i < v[offset].size(); i++) {
			t += CountAllChildren (v, c, v[offset][i]);
		}
		c[offset] = t + 1;
	}
	return c[offset];
}

int main (void) {
	int n, m, t1, t2, total = 0;
	cin >> n >> m;
	int Childrens[n];
	zero(Childrens);
	vector<int> Edges[n];
	for (int i = 0; i < m; i++) {
		cin >> t1 >> t2;
		Edges[--t2].push_back(--t1);
	}
	CountAllChildren (Edges, Childrens, 0);
	for (int i = 1; i < n; i++) {
		if (Childrens[i] % 2 == 0) {
			total += 1;
		}
	}
	cout << total << endl;
	return 0;
}
