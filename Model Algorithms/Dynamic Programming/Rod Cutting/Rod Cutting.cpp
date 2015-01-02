/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Getting the Maximum price obtained by cutting a rod using Tabulation (Bottom Up)
*/

/* Problem Statement: Given a rod of length of n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine the maximum value obtainable by 
*  cutting up the rod and selling the pieces.
*/

/* Time Complexity: O(n^2) */

#include <bits/stdc++.h>

using namespace std;

int RodCut (vector<int> &price, int n) {
	int value[n + 1];
	value[0] = 0;
	for (int i = 1; i <= n; i++) {
		int MaxValue = INT_MIN;
		for (int j = 0; j < i; j++) {
			MaxValue = max(MaxValue, price[j] + value[i - j - 1]);
		}
		value[i] = MaxValue;
	}
	return value[n];
}

int main (void) {
	int n, pr;
	cout << "Enter the length of rod and an array of prices that contains prices of all pieces of size smaller than n:" << endl;
	cin >> n;
	vector<int> price;
	for (int i = 0; i < n; i++) {
		cin >> pr;
		price.push_back(pr);
	}
	cout << "The maximum price obtained by cutting up the rod and selling the pieces is:" << RodCut(price, n) << endl;
	price.erase(price.begin(), price.end());
	return 0;
}
