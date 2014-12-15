/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/495/problem/A 
*  Algorithms: Implementation
*/

#include <bits/stdc++.h>

using namespace std;

int count (int n) {
	int type;
	switch(n){
		case 0:	type = 2;
				break;
		case 1:	type = 7;
				break;
		case 2:	type = 2;
				break;
		case 3:	type = 3;
				break;
		case 4:	type = 3;
				break;
		case 5:	type = 4;
				break;
		case 6:	type = 2;
				break;
		case 7:	type = 5;
				break;
		case 8:	type = 1;
				break;
		case 9:	type = 2;
				break;
	}
	return type;
}

int main (void) {
	int n, unit, ten;
	cin >> n;
	ten = n / 10;
	unit = n % 10;
	ten = count(ten);
	unit = count(unit);
	cout << ten * unit << endl;
	return 0;
}
