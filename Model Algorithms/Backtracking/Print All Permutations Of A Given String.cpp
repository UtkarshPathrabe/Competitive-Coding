/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Backtracking */

/* Problem Statement: Program to print all permutations of a given string */
/* Time Complexity: O(n * (n!)) */

#include <bits/stdc++.h>

using namespace std;

void Swap (char * a, char * b) {
	char temp = *a;
	*a = *b;
	*b = temp;
}

void Permute (char * str, int start, int end) {
	if (start == end) {
		cout << str << endl;
	} else {
		for (int i = start; i <= end; i++) {
			Swap ((str + start), (str + i));
			Permute (str, start + 1, end);
			Swap ((str + start), (str + i));	// Backtrack
		}
	}
}

int main (void) {
	char str[100];
	int n;
	cout << "Enter any String of alphabets and its length:" << endl;
	cin >> str >> n;
	Permute (str, 0, n - 1);
	return 0;
}
