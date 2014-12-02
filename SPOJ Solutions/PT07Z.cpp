/* Author: Utkarsh Pathrabe
*  Question can be found at: http://www.spoj.com/problems/PT07Z/
*  Algorithms: DFS
*/

#include <bits/stdc++.h>

using namespace std;

#define MAX 100009

bool check[ MAX ] = {false};
int total = 0;

int dfs( vector<int> v[], int root ) {
    int m, m1 = -1, m2 = -1;
    check[root] = 1;
    for(int i=0; i<v[root].size(); i++) {
        if(!check[v[root][i]]) {
            m = dfs(v,v[root][i]);
            if(m >= m1) {
                m2 = m1;
                m1 = m;
            }
            else if(m > m2)
                m2 = m;
        }
    }
    total = max(total, m1 + m2 + 2);
    return (m1 + 1);
}

int main() {
    int n, a, b;
    cin >> n;
    vector<int> v[n + 9];
    for(int i=0; i<n-1; i++) {
        scanf("%d %d", &a, &b);
        v[a].push_back(b);
        v[b].push_back(a);
    }
    dfs(v, 1);
    cout << total << endl;
	return 0;
}
