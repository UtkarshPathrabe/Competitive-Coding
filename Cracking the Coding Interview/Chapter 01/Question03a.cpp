/* Question03: Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
 NOTE: One or two additional variables are fine. An extra copy of the array is not. */
/* @Author: Utkarsh Pathrabe */
/* Time Complexity: O(N^2), Space Complexity: O(1) */

#include <bits/stdc++.h>

using namespace std;

void removeDuplicates (char str[]) {
	if (str == NULL) return;
	int tail = 1, i = 1, j;
	while (str[i] != '\0') {
		for (j = 0; j < tail; j++) {
			if (str[i] == str[j]) break;
		}
		if (j == tail) {
			str[tail++] = str[i];
		}
		i++;
	}
	str[tail] = '\0';
}

int main (void) {
	char str[] = "ababaabbbbcdecfgfh";
	cout << str << " after removing duplicates is ";
	removeDuplicates(str);
	cout << str << endl;
	return 0;
}
