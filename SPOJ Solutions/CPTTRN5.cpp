#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int test, l, c, s;
	bool flag;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		cin >> l >> c >> s;
		flag = false;
		for (int i = 0; i < ((s+1)*l + 1); i++) {
			for (int j = 0; j < ((s+1)*c + 1); j++) {
				if ((i%(s+1) == 0) || (j%(s+1) == 0)) {
					cout << "*";
				} else {
					if (flag) {
						if (((i-((int)i/(int)(s+1)))+(j-((int)j/(int)(s+1))))%s == 0) {
							cout << "\\";
						} else {
							cout << ".";
						}
					} else {
						if (((i-((int)i/(int)(s+1)))+(j-((int)j/(int)(s+1))))%s == 0) {
							cout << "/";
						} else {
							cout << ".";
						}
					}
				}
				if (j%(s+1) == 0) {
					flag = !flag;
				}
			}
			cout << endl;
		}
		cout << endl;
	}
	return 0;
}
