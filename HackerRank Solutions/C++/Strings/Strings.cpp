#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a + b << endl;
    char firstA = a[0], firstB = b[0];
    b[0] = firstA;
    a[0] = firstB;
    cout << a << " " << b << endl;
    return 0;
}
