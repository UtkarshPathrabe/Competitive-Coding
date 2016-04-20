#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    set<int> Set;
    set<int>::iterator it;
    int Q, y, x;
    scanf("%d", &Q);
    for (int i = 0; i < Q; i++) {
        scanf("%d %d", &y, &x);
        if (y == 1) {
            Set.insert(x);
        } else if (y == 2) {
            Set.erase(x);
        } else if (y == 3) {
            it = Set.find(x);
            if (it == Set.end()) {
                printf("No\n");
            } else {
                printf("Yes\n");
            }
        }
    }
    return 0;
}
