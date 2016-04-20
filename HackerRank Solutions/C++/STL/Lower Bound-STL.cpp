#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr;
    vector<int>::iterator it;
    int N, Q, Y;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int temp;
        scanf("%d", &temp);
        arr.push_back(temp);
    }
    scanf("%d", &Q);
    for (int i = 0; i < Q; i++) {
        scanf("%d", &Y);
        it = lower_bound(arr.begin(), arr.end(), Y);
        if (*it == Y) {
            printf("Yes %d\n", (it - arr.begin() + 1));
        } else {
            printf("No %d\n", (it - arr.begin() + 1));
        }
    }
    return 0;
}
