#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N;
	string s;
	cin >> N;
	getline (cin, s);
	while (N--) {
		getline (cin, s);
		if ((s[0] == 'H' || s[0] == 'h') && (s[1] == 'I' || s[1] == 'i') && (s[2] == ' ') && (s[3] != 'D' && s[3] != 'd')) {
			cout << s << endl;
		}
	}
	return 0;
}
