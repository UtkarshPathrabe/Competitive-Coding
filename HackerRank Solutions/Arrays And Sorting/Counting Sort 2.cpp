#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, Count[100] = {0}, temp;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		Count[temp] += 1;
	}
	for (int i = 0; i < 100; i++) {
		while (Count[i]--) {
			cout << i << " ";
		}
	}
	cout << endl;
	return 0;
}
