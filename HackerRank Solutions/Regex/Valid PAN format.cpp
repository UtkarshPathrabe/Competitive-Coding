#include <bits/stdc++.h>

using namespace std;

bool isDigit (char x) {
	if (x >= '0' && x <= '9')
		return true;
	return false;
}

bool isCapChar (char x) {
	if (x >= 'A' && x <= 'Z')
		return true;
	return false;
}

int main (void) {
	int N;
	bool flag = false;
	cin >> N;
	while (N--) {
		string s;
		cin >> s;
		flag = false;
		if (s.length() == 10) {
			for (int i = 0; i < 10; i++) {
				if ((i >= 0 && i < 5) || (i == 9)) {
					if (isCapChar (s[i]))
						flag = true;
					else {
						flag = false;
						break;
					}
				}
				if (i >= 5 && i < 9) {
					if (isDigit (s[i]))
						flag = true;
					else {
						flag = false;
						break;
					}
				}
			}
		}
		if (flag) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
	return 0;
}
