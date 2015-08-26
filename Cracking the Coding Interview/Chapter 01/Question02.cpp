/* Question02: Write code to reverse a C-Style String.
 (C-String means that “abcd” is represented as five characters, including the null character.) */
/* @Author: Utkarsh Pathrabe */
/* Time Complexity: O(n), Space Complexity: O(1) */

#include <bits/stdc++.h>

using namespace std;

void reverse (char *string) {
	char *end = string, temp;
	if (string) {
		while (*end) {
			++end;
		}
		--end;
		while (string < end) {
			temp = *string;
			*string++ = *end;
			*end-- = temp;
		}
	}
}

int main (void) {
	char s[] = "abcdefgh";
	cout << s << " after reversing is ";
	reverse(s);
	cout << s << endl;
	return 0;
}
