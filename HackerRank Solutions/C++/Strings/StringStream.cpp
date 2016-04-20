#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> temp;
    char tempChar;
    int tempInt;
    stringstream s(str);
    while(s >> tempInt) {
        temp.push_back(tempInt);
        s >> tempChar;
    }
    return temp;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    return 0;
}
