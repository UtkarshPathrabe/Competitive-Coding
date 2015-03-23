#include <bits/stdc++.h>

using namespace std;

vector<int> Weight;

int main (void) {
	int N, weight, unit = 0, i;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> weight;
		Weight.push_back(weight);
	}
	sort(Weight.begin(), Weight.end());
	i = *Weight.begin();
	while (Weight.size() != 0) {
		unit++;
		while ((Weight.size() != 0) && (*Weight.begin() <= i+4)) {
			Weight.erase(Weight.begin(), Weight.begin() + 1);
		}
		if (Weight.size() != 0) {
			i = *Weight.begin();
		} else {
			break;
		}
	}
	cout << unit << endl;
	return 0;
}
