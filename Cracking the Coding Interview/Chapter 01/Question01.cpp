/* Question01: Implement an algorithm to determine if a string has all unique characters.
 What if you can not use additional data structures? */
/* @Author: Utkarsh Pathrabe */
/* Time Complexity: O(n), Space Complexity: O(n) */

#include <bits/stdc++.h>

using namespace std;

bool hasUnique (string s) {
	bool flag[256] = {false};
	for (int i = 0; i < s.length(); i++) {
		int value = s[i];
		if (flag[value]) return false;
		flag[value] = true;
	}
	return true;
}

int main (void) {
	string s = "Utkarsh!";
	if (hasUnique(s)) {
		cout << s << " has all unique characters." << endl;
	} else {
		cout << s << " does not have all unique characters." << endl;
	}
	return 0;
}
