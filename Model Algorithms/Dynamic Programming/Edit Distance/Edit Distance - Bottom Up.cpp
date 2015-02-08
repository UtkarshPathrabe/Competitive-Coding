#include <bits/stdc++.h>
#define N 100

using namespace std;

string s1, s2;
int edit[2][N] = {{0}};

int Edit () {
	for (int i = 0; i < N; i++) {
		edit[0][i] = i; 
	}
	for (int i = 1; i <= s1.length(); i++) {
		for (int j = 0; j <= s2.length(); j++) {
			if (j == 0) {
				edit[i%2][j] = i;
			} else {
				edit[i%2][j] = min (min (edit[(i-1)%2][j] + 1, edit[i%2][j-1]+1), edit[(i-1)%2][j-1] + ((s1[i-1] == s2[j-1]) ? 0 : 1));
			}
		}
	}
	return edit[s1.length()%2][s2.length()];
}

int main (void) {
	cin >> s1 >> s2;
	cout << Edit () << endl;
	return 0;
}
