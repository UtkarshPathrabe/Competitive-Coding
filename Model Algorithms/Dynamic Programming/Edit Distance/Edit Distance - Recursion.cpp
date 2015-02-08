#include <bits/stdc++.h>

using namespace std;

string s1, s2;

int EditDis (int i, int j) {
	if ((i >= 0) && (j >= 0)) {
		return min (min (EditDis (i, j - 1) + 1, EditDis (i - 1, j) + 1), EditDis (i - 1, j - 1) + ((s1[i] == s2[j]) ? 0 : 1));
	}
	return 0;
}

int main (void) {
	cin >> s1 >> s2;
	cout << EditDis (s1.length() - 1, s2.length() -1) << endl;
	return 0;
}
