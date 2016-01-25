#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int t;
	cin >> t;
	while (t--) {
		string str;
		cin >> str;
		int len = str.length() / 2;
		for (int i = 0; i < len; i += 2) {
			cout << str[i];
		}
		cout << endl;
	}
	return 0;
}
