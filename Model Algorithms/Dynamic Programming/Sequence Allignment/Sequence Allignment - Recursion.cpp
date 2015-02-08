#include <bits/stdc++.h>
#define GAP -1
#define MATCH 2
#define MISMATCH -2

using namespace std;

string s1, s2;

int NWScore (int i, int j) {
	if (i >= 0 && j >= 0) {
		return max (max (NWScore (i, j - 1) + GAP, NWScore (i - 1, j) + GAP), NWScore (i - 1, j - 1) + ((s1[i] == s2[j]) ? MATCH:MISMATCH));
	}
	return 0;
}

int main (void) {
	cin >> s1 >> s2;
	cout << NWScore (s1.length() - 1, s2.length() - 1) << endl;
	return 0;
}
