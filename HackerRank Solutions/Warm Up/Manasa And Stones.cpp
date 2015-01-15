#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, n, a, b;
	cin >> T;
	while (T--) {
		cin >> n >> a >> b;
		set<int> first, second;
		set<int> :: iterator it;
		first.insert(0); 
		for (int i = 1; i < n; i++) {
			if (i % 2 == 1) {
				second.erase(second.begin(), second.end());
				for (it = first.begin(); it != first.end(); it++) {
					second.insert((*it) + a);
					second.insert((*it) + b);
				}
			} else {
				first.erase(first.begin(), first.end());
				for (it = second.begin(); it != second.end(); it++) {
					first.insert((*it) + a);
					first.insert((*it) + b);
				}
			}
		}
		if ((n - 1) % 2 == 1) {
			for (it = second.begin(); it != second.end(); it++) {
				cout << (*it) << " ";
			}
			cout << endl;
		} else {
			for (it = first.begin(); it != first.end(); it++) {
				cout << (*it) << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
