#include <bits/stdc++.h>
#define N 100
#define GAP -1
#define MATCH 2
#define MISMATCH -2

using namespace std;

string s1, s2;
int sim[N][N] = {{0}};
stack<char> st1, st2;

void PrintAllignment () {
	int i = s1.length(), j = s2.length();
	while ((i > 0) && (j > 0)) {
		if ((sim[i-1][j-1] > sim[i][j-1]) && (sim[i-1][j-1] > sim[i-1][j])) {
			i -= 1;
			j -= 1;
			st1.push(s1[i]);
			st2.push(s2[j]);
		} else if ((sim[i-1][j] > sim[i-1][j-1]) && (sim[i-1][j] > sim[i][j-1])) {
			i -= 1;
			st1.push(s1[i]);
			st2.push(' ');
		} else {
			j -= 1;
			st1.push(' ');
			st2.push(s2[j]);
		}
	}
	while (!st1.empty()) {
		cout << st1.top();
		st1.pop();
	}
	cout << endl;
	while (!st2.empty()) {
		cout << st2.top();
		st2.pop();
	}
	cout << endl;
}

int NWScore () {
	for (int i = 0; i < N; i++) {
		sim[i][0] = i * GAP;
		sim[0][i] = i * GAP;
	}
	for (int i = 1; i <= s1.length(); i++) {
		for (int j = 1; j <= s2.length(); j++) {
			sim[i][j] = max (max (sim[i][j - 1] + GAP, sim[i - 1][j] + GAP), sim[i - 1][j - 1] + ((s1[i - 1] == s2[j - 1]) ? MATCH : MISMATCH));
		}
	}
	return sim[s1.length()][s2.length()];
}

int main (void) {
	cin >> s1 >> s2;
	cout << NWScore () << endl;
	PrintAllignment ();
	return 0;
}
