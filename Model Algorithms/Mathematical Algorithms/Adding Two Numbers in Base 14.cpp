/* Author: Utkarsh Ashok Patharbe
*  Algorithm: Mathematical Algorithms
*/

/* Time Complexity: O(n) where n is the length of input integer in base 14 */

#include <bits/stdc++.h>
#define N 100

using namespace std;

char Number1[N], Number2[N], Sum[N];

int GetNumeralValue (char Numeral) {
	if ((Numeral >= '0') && (Numeral <= '9')) {
		return (Numeral - '0');
	} else if ((Numeral >= 'A') && (Numeral <= 'D')) {
		return (Numeral - 'A' + 10);
	} else {
		assert (0);
	}
}

char GetNumeral (int Number) {
	if ((Number >= 0) && (Number <= 9)) {
		return (Number + '0');
	} else if ((Number >= 10) && (Number <= 14)) {
		return (Number - 10 + 'A');
	} else {
		assert (0);
	}
}

void Equalize (int len, int len1, int len2) {
	if (len != len1) {
		for (int i = len - 1, j = len1 - 1; i >= 0; i--, j--) {
			if (j >= 0) {
				Number1[i] = Number1[j];
			} else {
				Number1[i] = '0';
			}
		}
	} else {
		for (int i = len - 1, j = len2 - 1; i >= 0; i--, j--) {
			if (j >= 0) {
				Number2[i] = Number2[j];
			} else {
				Number2[i] = '0';
			}
		}
	}
}

char* AddBase14 () {
	int len1 = strlen(Number1);
	int len2 = strlen(Number2);
	int carry = 0, num1 = 0, num2 = 0, len = max(len1, len2), result = 0;
	if (len1 != len2) {
		Equalize (len, len1, len2);
	}
	for (int i = len - 1; i >= 0; i--) {
		num1 = GetNumeralValue (Number1[i]);
		num2 = GetNumeralValue (Number2[i]);
		result = carry + num1 + num2;
		if (result >= 14) {
			carry = 1;
			result -= 14;
		} else {
			carry = 0;
		}
		Sum[i + 1] = GetNumeral(result);
	}
	if (carry == 1) {
		Sum[0] = '1';
	} else {
		Sum[0] = '0';
	}
	return Sum;
}

int main (void) {
	cout << "Enter two numbers in base 14:" << endl;
	cin >> Number1 >> Number2;
	cout << "The Sum is: " << AddBase14() << endl;
	return 0;
}
