#include <bits/stdc++.h>

using namespace std;

bool strEquals (string s1, string s2) {
	if (s1.length() == s2.length()) {
		for (int i = 0; i < s1.length(); i++) {
			if (toupper(s1[i]) != toupper(s2[i])) {
				return false;
			}
		}
		return true;
	} else {
		return false;
	}
}

int main (void) {
	int N, count = 0;
	string s, buff = "HACKERRANK";
	cin >> N;
	getline (cin, s);
	while (N--) {
		getline (cin, s);
		for (int i = 0; i < s.length(); i++) {
			if (strEquals (buff, s.substr(i, 10))) {
				count++;
				break;
			}
		}
	}
	cout << count << endl;
	return 0;
}
