#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, temp;
	cin >> n;
	vector< pair<int, string> > data, output;
	string str;
	int Count[100] = {0};
	for (int i = 0; i < n; i++) {
		cin >> temp >> str;
		Count[temp] += 1;
		if (i < (n / 2)) {
			data.push_back(make_pair(temp, "-"));
		} else {
			data.push_back(make_pair(temp, str));
		}
		output.push_back(make_pair(-1, ""));
	}
	for (int i = 1; i < 100; i++) {
		Count[i] += Count[i - 1];
	}
	for (int i = n - 1; i >= 0; i--) {
		output[Count[data[i].first] - 1] = data[i];
		Count[data[i].first] -= 1;
	}
	for (int i = 0; i < n; i++) {
		cout << output[i].second << " ";
	}
	cout << endl;
	return 0;
}
