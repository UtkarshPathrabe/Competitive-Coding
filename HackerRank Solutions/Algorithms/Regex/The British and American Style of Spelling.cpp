#include <bits/stdc++.h>

using namespace std;

bool strEquals (string s1, string s2) {
	if (s1.length() == s2.length()) {
		for (int i = 0; i < s1.length(); i++) {
			if (s1[i] != s2[i]) {
				if ((i == s1.length() - 2) && (s1[i] == 'z' || s1[i] == 's') && (s2[i] == 'z' || s2[i] == 's'))
					continue;
				else
					return false;
			}
		}
		return true;
	} else {
		return false;
	}
}

int main (void) {
	int N, count = 0, T;
	string s[10], buff;
	cin >> N;
	getline (cin, buff);
	for (int i = 0; i < N; i++) {
		getline (cin, s[i]);	
	}
	cin >> T;
	getline (cin, buff);
	while (T--) {
		getline (cin, buff);
		count = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < s[i].length(); j++) {
				if (strEquals (buff, s[i].substr(j, buff.length()))) {
					count++;
				}
			}
		}
		cout << count << endl;
	}
	return 0;
}
