/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/493/problem/B 
*  Algorithms: Implementation
*/

#include <bits/stdc++.h>

using namespace std;

vector <long long int> first;
vector <long long int> second;

int compare(vector<long long int> &f, vector<long long int> &s) {
	int i;
	for(i = 0; (i < f.size()) && (i < s.size()); i++){
		if(f[i] > s[i])
			return 1;
		else if(f[i] < s[i])
			return -1;
	}
	if(i == f.size() && i != s.size())
		return -1;
	else if(i != f.size() && i == s.size())
		return 1;
	else
		return 0;
}

int main(void) {
	int n;
	long long int sum = 0, a;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		scanf("%lld", &a);
		sum += a;
		if(a > 0)
			first.push_back(abs(a));
		else
			second.push_back(abs(a));
	}
	if(sum > 0)
		printf("first\n");
	else if(sum < 0)
		printf("second\n");
	else{
		int val = compare(first, second);
		if(val == 1)
			printf("first\n");
		else if(val == -1)
			printf("second\n");
		else{
			if(a >= 0)
				printf("first\n");
			else
				printf("second\n");
		}
	}
	return 0;
}
