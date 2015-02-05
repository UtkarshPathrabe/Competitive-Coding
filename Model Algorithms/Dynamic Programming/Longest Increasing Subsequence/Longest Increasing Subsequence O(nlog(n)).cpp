/* Author: Utkarsh Ashok Pathrabe
*  Problem Statement: Given an array of random numbers. 
*  			Find longest monotonically increasing subsequence (LIS) in the array.
*/

/* Time Complexity: O(n * log(n)) */

#include <bits/stdc++.h>

using namespace std;

int GetCeilPos (vector<int> &A, vector<int> &T, int left, int right, int key) {
	while (right - left > 1) {
		int mid = left + (right - left) / 2;
		if (A[T[mid]] >= key) {
			right = mid;
		} else {
			left = mid;
		}
	}
	return right;
}

int LIS (vector<int> &A) {
	vector<int> tailInd(A.size());
	vector<int> prevInd(A.size());
	stack<int> out;
	int len = 1;
	for (int i = 0; i < A.size(); i++) {
		tailInd[i] = 0;
		prevInd[i] = 0;
	}
	tailInd[0] = 0;
	prevInd[0] = -1;
	for (int i = 1; i < A.size(); i++) {
		if (A[i] < A[tailInd[0]]) {
			tailInd[0] = i;
		} else if (A[i] > A[tailInd[len - 1]]) {
			prevInd[i] = tailInd[len - 1];
			tailInd[len++] = i;
		} else {
			int pos = GetCeilPos (A, tailInd, -1, len - 1, A[i]);
			prevInd[i] = tailInd[pos - 1];
			tailInd[pos] = i;
		}
	}
	for (int i = tailInd[len - 1]; i >= 0; i = prevInd[i]) {
		out.push(A[i]);
	}
	while (!out.empty()) {
		cout << out.top() << " ";
		out.pop();
	}
	cout << endl;
	tailInd.erase(tailInd.begin(), tailInd.end());
	prevInd.erase(prevInd.begin(), prevInd.end());
	return len;
}

int main (void) {
	int N, temp;
	cin >> N;
	vector<int> D;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		D.push_back(temp);
	}
	cout << LIS (D);
	return 0;
}
