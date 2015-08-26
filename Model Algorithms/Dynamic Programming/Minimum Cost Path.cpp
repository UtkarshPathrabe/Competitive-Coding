/* Time Complexity: O(m*n); Space Complexity: O(min(m, n)) */

#include <bits/stdc++.h>

using namespace std;

int minCost (vector < vector <int> > &cost, int m, int n) {
	int temp[2][n+1];
	temp[0][0] = cost[0][0];
	for (int i = 1; i <= n; i++) {
		temp[0][i] = temp[0][i-1] + cost[0][i];
	}
	for (int i = 1; i <= m; i++) {
		for (int j = 0; j <= n; j++) {
			if (j == 0) {
				temp[i%2][j] = temp[(i-1)%2][j] + cost[i][j];
			} else {
				temp[i%2][j] = min (min (temp[(i-1)%2][j], temp[i%2][j-1]), temp[(i-1)%2][j-1]) + cost[i][j];
			}
		}
	}
	return temp[m%2][n];
}

int main (void) {
	vector < vector <int> > cost;
	vector <int> temp;
	temp.push_back (1);
	temp.push_back (2);
	temp.push_back (3);
	cost.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (4);
	temp.push_back (8);
	temp.push_back (2);
	cost.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (1);
	temp.push_back (5);
	temp.push_back (3);
	cost.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	int m = 2, n = 2;
	cout << "The cost of minimum path from (0, 0) to (" << m << ", " << n << ") is " << minCost (cost, m, n) << "." << endl;
	return 0;
}
