#include <bits/stdc++.h>

using namespace std;

int UnboundedKnapSack (vector<int> &value, vector<int> &weight, int n, int W) {
	int Max[W + 1], temp;
	for (int i = 0; i <= W; i++) {
		Max[i] = 0;
	}
	for (int i = 1; i <= W; i++) {
		Max[i] = Max[i - 1];
		for (int j = 0; j < n; j++) {
			if (i >= weight[j]) {
				temp = Max[i - weight[j]] + value[j];
			}
			if (temp > Max[i]) {
				Max[i] = temp;
			}
		}
	}
	return Max[W];
}

int main (void) {
	int W, n;
	cout << "Enter the number of items and the maximum capacity:" << endl;
	cin >> n >> W;
	vector<int> val;
	vector<int> wt;
	for (int i = 0; i < n; i++) {
		int v, w;
		cout << "Enter value and weight of " << (i + 1) << " item:" << endl;
		cin >> v >> w;
		val.push_back(v);
		wt.push_back(w);
	}
	cout << "The maximum sum of values that we can get (given the restrictions on weights) is:" << UnboundedKnapSack(val, wt, n, W) << endl;
	val.erase(val.begin(), val.end());
	wt.erase(wt.begin(), wt.end());
	return 0;
}
