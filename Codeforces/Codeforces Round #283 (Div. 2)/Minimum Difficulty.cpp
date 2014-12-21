/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/496/problem/A
*  Algorithms: Brute Force, Implementation
*/

#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int arr[1000];
    int n, min, max, op, np;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    min = arr[n - 1] - arr[0];
    for(int i = 1; i < (n - 1); i++){
        max = 0;
        op = 0;
        for(int j = 1; j < n; j++){
                if(j == i) 
					continue;
                np = j;
                if(max < (arr[np] - arr[op])) 
					max = arr[np] - arr[op];
                op = np;
        }
        if(min > max) 
			min = max;
    }
    cout << min << endl;
    return 0;
}
