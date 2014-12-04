/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/493/problem/D 
*  Algorithms: Constructive Algorithms, Games
*/

#include <bits/stdc++.h>

using namespace std;

int main(void) {
	long long int n;
	cin >> n;
	if((n % 2) == 1)
		printf("black\n");
	else{
		printf("white\n1 2\n");
	}
	return 0;
}
