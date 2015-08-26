#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    int T, minCount;
    cin >> T;
    while (T--) {
        int N, min = INT_MAX, count = 0;
        minCount = INT_MAX;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        for (int i = 0; i <= 5; i++) {
            count = 0;
            for (int j = 0; j < N; j++) {
                int V = arr[j] - (min - i);
                int X = V % 5;
                count += (V / 5) + (X / 2) + (X & 1);
            }
            if (minCount > count) {
                minCount = count;
            }
        }
        cout << minCount << endl; 
    }
    return 0;
}
