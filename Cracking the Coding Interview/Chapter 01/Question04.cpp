/* Question04: Write a method to decide if two strings are anagrams or not. */
/* @Author: Utkarsh Pathrabe */
/* Time Complexity: O(n*log(n)), Space Complexity: O(1) */

#include <bits/stdc++.h>

using namespace std;

bool isEqual (char s1[], char s2[]) {
	if (strlen(s1) != strlen(s2)) return false; 
	for (int i = 0; (i < strlen(s1)); i++) {
		if (s1[i] != s2[i]) return false;
	}
	return true;
}

int partition (char s[], int p, int r) {
	char x = s[r];
	int i = p - 1;
	char t;
	for (int j = p; j < r; j++) {
		if (s[j] <= x) {
			i = i + 1;
			t = s[i];
			s[i] = s[j];
			s[j] = t;
		}
	}
	t = s[i + 1];
	s[i + 1] = s[r];
	s[r] = t;
	return i + 1;
}

void quicksort (char s[], int p, int r) {
	if (p < r) {
		int q = partition (s, p, r);
		quicksort (s, p, q - 1);
		quicksort (s, q + 1, r);
	}
}

bool isAnagram (char s1[], char s2[]) {
	quicksort(s1, 0, strlen(s1) - 1);
	quicksort(s2, 0, strlen(s2) - 1);
	return isEqual(s1, s2);
}

int main (void) {
	char s1[] = "holo";
	char s2[] = "oloh";
	cout << s1 << " and " << s2 << " are";
	if (isAnagram(s1, s2)) {
		cout << " anagrams." << endl;
	} else {
		cout << " not anagrams." << endl;
	}
	return 0;
}
