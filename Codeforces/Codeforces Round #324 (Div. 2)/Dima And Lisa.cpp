#include <bits/stdc++.h>

typedef long long int LLI;

using namespace std;

bool isPrime (LLI n) {
	if (n <= 1) return false;
	if (n == 2) return true;
    if (n%2 == 0) return false;
	int m = (LLI)sqrt((double)n);
	for (LLI i = 3; i <= m; i += 2){
        if (n % i == 0)
			return false;
    }
    return true;
}

int main (void) {
	LLI num;
	cin >> num;
	if ((num == 3) || (num == 5) || (num == 7)) {
		cout << "1" << endl << num << endl;
	} else {
		cout << "3" << endl << "3 ";
		for (LLI i = 3; ; i += 2) {
			if (isPrime(i)) {
				LLI j = num - 3 - i;
				if (isPrime(j)) {
					cout << i << " " << j << endl;
					break;
				}
			}
		}
	}
	return 0;
}
