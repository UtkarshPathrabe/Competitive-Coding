/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/496/problem/C
*  Algorithms: Brute Force, Implementation, Constructive Algorithms
*/

#include <bits/stdc++.h>

using namespace std;

int n, m, ans = 0;

string a[105];
vector<char> b[105];

int main (void) {
    int i, j;
    cin >> n >> m;
    for (i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (j = 0; j < m; j++) {
        for (i = 0; i < n; i++) {
            b[i].push_back(a[i][j]);
        }
        for (i = 1; i < n; i++) {
            if (b[i] < b[i - 1]) 
				break;
        }
        if (i < n) {
            ans++;
            for (i = 0; i < n; i++) {
                b[i].pop_back();
            }
        }
    }
    cout << ans << endl;
    return 0;
}
