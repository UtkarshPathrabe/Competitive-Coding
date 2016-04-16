#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N;
    string name, phone;
    map<string, string> phoneBook;
    map<string, string>::iterator it;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> name >> phone;
        phoneBook[name] = phone;
    }
    getline(cin, name);
    while (getline(cin, name)) {
    	it = phoneBook.find(name);
		if (it != phoneBook.end()) {
			cout << name << "=" << phoneBook[name] << endl;
		} else {
			cout << "Not found" << endl;
		}
    }
    return 0;
}

