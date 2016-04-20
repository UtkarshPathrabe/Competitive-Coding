#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr;
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int temp;
        scanf("%d", &temp);
        arr.push_back(temp);
    }
    sort(arr.begin(), arr.end());
    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
