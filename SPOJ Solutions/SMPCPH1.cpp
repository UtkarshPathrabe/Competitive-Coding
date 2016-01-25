#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int n, m;
	cin >> n;
	char seq[n+1], buff[2];
	cin >> seq;
	map <char, char> mymap;
	map <char, char> :: iterator itmap;
	for (int i = 0; i < n; i++) {
		mymap[seq[i]] = seq[(i+1)%n];
	}
	cin >> m;
	gets (buff);
	for (int i = 0; i < m; i++) {
		char text[1005] = {'\0'};
		gets (text);
		for (int j = 0; text[j] != '\0'; j++) {
			itmap = mymap.find (text[j]);
			if (itmap != mymap.end()) {
				cout << itmap->second;
			} else {
				cout << text[j];
			}
		}
		cout << endl;
	}
	return 0;
}
