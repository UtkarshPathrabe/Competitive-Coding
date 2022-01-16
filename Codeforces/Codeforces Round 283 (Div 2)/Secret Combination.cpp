/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/496/problem/B
*  Algorithms: Brute Force, Implementation, Constructive Algorithms
*/

#include<bits/stdc++.h>

using namespace std;

int main (void) {
    int d, n, k;
    cin >> n;
    string a, mx, tmp, tmp1;
    cin >> a;
    mx = a;
    for(int i = 0; i < n; i++) {
        tmp = a;
        d = 10 - (tmp[i] - '0');
        for(int j = 0; j < n; j++){
            tmp[j] = (((tmp[j] - '0') + d) % 10) + '0';
        }
        tmp1 = a;
        k = 0;
        for(int j = i; j < n; j++){
            tmp1[k++] = tmp[j];
        }
        for(int j = 0; j < i; j++){
            tmp1[k++] = tmp[j];
        }
        if(mx > tmp1){
            mx = tmp1;
        }
    }
    cout << mx << endl;  
    return 0;
}
