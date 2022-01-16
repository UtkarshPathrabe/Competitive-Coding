/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/495/problem/B 
*  Algorithms: Math
*/

#include <bits/stdc++.h>

using namespace std;

int main (void) {
	long long int a, b, n, count = 0, i;
	cin >> a >> b;
	n = a - b;
	if(n == 0) {
		cout << "infinity" << endl;
	} else if (n < 0) {
		cout << "0" << endl;
	} else {
		for (i = 1; i < sqrt(n); i++) {
			if ((n % i) == 0) {
				if (i > b)
					count += 1;
				if ((n / i) > b)
					count += 1;
			}
		}
		if (((i * i) == n) && (i > b))
			count += 1;
		cout << count << endl;
	}
	return 0;
}
