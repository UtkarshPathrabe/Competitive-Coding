#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;
    vector<int> rating;
    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        rating.push_back(x);
    }
    vector<int> Left(N, 1);
    vector<int> Right(N, 1);
    for (int i = 1; i < N; i++) {
        if (rating[i] > rating[i-1]) {
            Left[i] = 1 + Left[i-1];
        }
    }
    for (int i = N-2; i >= 0; i--) {
        if (rating[i] > rating[i+1]) {
            Right[i] = 1 + Right[i+1];
        }
    }
    int candy = 0;
    for (int i = 0; i < N; i++) {
        candy += max(Left[i], Right[i]);
    }
    printf ("%d", candy);
    return 0;
}
