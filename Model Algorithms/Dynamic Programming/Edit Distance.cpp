/* Time Complexity: O(m*n); Space Complexity: O(min(m, n)) */

#include <bits/stdc++.h>
#define SPACE 1
#define MATCH 0
#define MISMATCH 1

using namespace std;

int EDIT (string s1, string s2) {
	int edit[2][s2.length()+1];
	for (int i = 0; i <= s2.length(); i++) {
		edit[0][i] = i;
	}
	for (int i = 1; i <= s1.length(); i++) {
		for (int j = 0; j <= s2.length(); j++) {
			if (j == 0) {
				edit[i%2][j] = i;
			} else {
				edit[i%2][j] = min (min (edit[(i-1)%2][j] + SPACE, edit[i%2][j-1] + SPACE), edit[(i-1)%2][j-1] + ((s1[i-1] == s2[j-1]) ? MATCH : MISMATCH));
			}
		}
	}
	return edit[s1.length()%2][s2.length()];
}

int main (void) {
	string s1 = "SUNDAY", s2 = "SATURDAY";
	cout << "Edit Distance of given strings is " << EDIT (s1, s2) << "." << endl;
	return 0;
}
