#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr;
    int N, x, a, b;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int temp;
        scanf("%d", &temp);
        arr.push_back(temp);
    }
    scanf("%d %d %d", &x, &a, &b);
    arr.erase(arr.begin()+x-1);
    arr.erase(arr.begin()+a-1, arr.begin()+b-1);
    printf("%d\n", arr.size());
    for (int i = 0; i < arr.size(); i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
