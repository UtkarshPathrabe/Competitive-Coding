#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int N;
	string s;
	cin >> N;
	getline (cin, s);
	while (N--) {
		string CountryCode, LocalAreaCode, Number;
		size_t pos1, pos2;
		getline (cin, s);
		pos1 = s.find ("-");
		if (pos1 == -1) {
			pos1 = s.find (" ");
		}
		pos2 = s.rfind ("-");
		if (pos2 == -1) {
			pos2 = s.rfind (" ");
		}
		CountryCode = s.substr (0, pos1);
		LocalAreaCode = s.substr (pos1 + 1, pos2 - pos1 - 1);
		Number = s.substr (pos2 + 1, s.length () - pos2);
		cout << "CountryCode=" << CountryCode << ",LocalAreaCode=" << LocalAreaCode << ",Number=" << Number << endl;
	}
	return 0;
}
