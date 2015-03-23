#include <bits/stdc++.h>

using namespace std;

bool flag[26] = {false};

bool IsPangram () {
	for (int i = 0; i < 26; i++) {
		if (!flag[i]) {
			return false;
		}
	}
	return true;
}

int main (void) {
	string s;
	int index;
	getline( cin, s);
	for (string::iterator it = s.begin(); it != s.end(); it++) {
		index = tolower(*it) - 'a';
		if ((index >= 0) && (index < 26)) {
			flag[index] = true;
		}
	}
	if (IsPangram ()) {
		cout << "pangram" << endl;
	} else {
		cout << "not pangram" << endl;
	}
	return 0;
}
