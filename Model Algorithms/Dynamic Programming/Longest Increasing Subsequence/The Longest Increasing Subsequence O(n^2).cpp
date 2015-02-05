/* Author: Utkarsh Ashok Pathrabe
*  Problem Statement: Given an array of random numbers. 
*  			Find longest monotonically increasing subsequence (LIS) in the array.
*/

/* Time Complexity: O(n ^ 2) */

#include <bits/stdc++.h>

using namespace std;

long long int LIS (vector<long long int> &D) {
	int Max = 1;
	vector < vector<int> > L(D.size());
	L[0].push_back(D[0]);
	for (int i = 1; i < D.size(); i++) {
		for (int j = 0; j < i; j++) {
			if ((D[j] < D[i]) && (L[i].size() < L[j].size() + 1)) {
				L[i] = L[j];
			}
		}
		L[i].push_back(D[i]);
		Max = (Max > L[i].size()) ? Max : L[i].size();
	}
	for (int i = 0; i < L[D.size() - 1].size(); i++) {
		cout << L[D.size() - 1][i] << " ";
	}
	cout << endl;
	return Max;
}

int main (void) {
	long long int N, temp;
	cin >> N;
	vector<long long int> D;
	for (long long int i = 0; i < N; i++) {
		cin >> temp;
		D.push_back(temp);
	}
	cout << LIS (D);
	return 0;
}
