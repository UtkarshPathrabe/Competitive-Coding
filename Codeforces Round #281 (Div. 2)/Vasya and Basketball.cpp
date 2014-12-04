/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/493/problem/C 
*  Algorithms: Binary Search, Brute Force, Implementation, Sorting, Two Pointer
*/

#include <bits/stdc++.h>

using namespace std;

vector <long long int> first;
vector <long long int> second;

int main(void) {
	int n, m;
	long long int a, b, scoreA, scoreB, maxA, maxB, maxDiff;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		cin >> a;
		first.push_back(a);
	}
	first.push_back(2087654321);
	scanf("%d", &m);
	for(int i = 0; i < m; i++) {
		cin >> b;
		second.push_back(b);
	}
	second.push_back(2087654321);
	sort(first.begin(), first.end());
	sort(second.begin(), second.end());
	maxA = scoreA = 3 * n;
	maxB = scoreB = 3 * m;
	maxDiff = scoreA - scoreB;
	for(int i = 0, j = 0; i < n || j < m; ) {
		if(first[i] < second[j]) {
			scoreA -= 1;
			i++;
		}else if(first[i] > second[j]) {
			scoreB -= 1;
			j++;
		}else {
			scoreA -= 1;
			scoreB -= 1;
			i++;
			j++;
		}
		if(scoreA - scoreB > maxDiff) {
			maxDiff = scoreA - scoreB;
			maxA = scoreA;
			maxB = scoreB;
		}
	}
	cout << maxA << ':' << maxB << endl;
	return 0;
}
