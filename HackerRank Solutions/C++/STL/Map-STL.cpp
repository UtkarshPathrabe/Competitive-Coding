#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main() {
    map<string, int> Map;
    map<string, int>::iterator it;
    int Q, Y, type;
    string X;
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> type >> X;
        if (type == 1) {
            cin >> Y;
            it = Map.find(X);
            if (it == Map.end()) {
                Map[X] = Y;
            } else {
                Map[X] += Y;
            }
        } else if (type == 2) {
            Map[X] = 0;
        } else if (type == 3) {
            cout << Map[X] << endl;
        }
    }
    return 0;
}
