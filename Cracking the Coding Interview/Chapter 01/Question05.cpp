/* Question05: Write a method to replace all spaces in a string with ‘%20’. */
/* @Author: Utkarsh Pathrabe */
/* Time Complexity: O(n), Space Complexity: O(1) */

#include <bits/stdc++.h>

using namespace std;

char *replace (char s[]) {
	int len = strlen(s), spacecount = 0, newlen;
	for (int i = 0; i < len; i++) {
		if (s[i] == ' ') spacecount++;
	}
	newlen = len + (spacecount * 2);
	char *s1 = (char *)malloc(sizeof(char) * (newlen + 1));
	s1[newlen] = '\0';
	for (int i = len - 1; i >= 0; i--) {
		if (s[i] == ' ') {
			s1[newlen - 1] = '0';
			s1[newlen - 2] = '2';
			s1[newlen - 3] = '%';
			newlen -= 3;
		} else {
			s1[newlen - 1] = s[i];
			newlen -= 1;
		}
	}
	return s1;
}

int main (void) {
	char s[] = "Hi How are you .";
	cout << s << " after replacing is " << replace(s) << endl;
	return 0;
}
