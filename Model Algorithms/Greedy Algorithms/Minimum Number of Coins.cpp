/* Problem: Given a value V, if we want to make change for V Rs, and we have infinite supply of each of the denominations in Indian currency, 
*  i.e., we have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, 
*  what is the minimum number of coins and/or notes needed to make the change?
*/

#include <bits/stdc++.h>

using namespace std;

void findMin (int V) {
	cout << "Following is the minimal number of change for " << V << ":" << endl;
	vector <int> ans;
	int denomination[] = {1, 2, 5, 10, 20, 50, 100, 500, 1000};
	int n = (sizeof (denomination)) / (sizeof (denomination[0]));
	for (int i = n-1; i >= 0; i--) {
		while (V >= denomination[i]) {
			V -= denomination[i];
			ans.push_back(denomination[i]);
		}
	}
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << "\t";
	}
	cout << endl;
}

int main () {
	findMin (1688);
	return 0;
}
