#include <bits/stdc++.h>
#define LLI long long int

using namespace std;

LLI max (LLI a, LLI b) {
	if (a - b >= 0) {
		return a;
	} else {
		return b;
	}
}

int main (void) {
	LLI n, d;
	cin >> n >> d;
	vector <pair <LLI, LLI> > data;
	for (int i = 0; i < n; i++) {
		LLI m, s;
		cin >> m >> s;
		data.push_back (make_pair(m, s));
	}
	sort (data.begin(), data.end());
	vector<LLI> sum(n+1, 0);
	for (LLI i = 1; i <= n; i++) {
		sum[i] = sum[i-1] + data[i-1].second;
	}
	LLI ffac = 0, j = 1;
	for (LLI i = 0; i < n; i++) {
		while ((j < n) && (data[i].first + d > data[j].first)) {
			j++;
		}
		ffac = max (ffac, sum[j] - sum[i]);
	}
	cout << ffac << endl;
	return 0;
}
