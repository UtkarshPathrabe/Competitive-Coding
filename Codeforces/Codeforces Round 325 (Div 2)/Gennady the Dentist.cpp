#include <bits/stdc++.h>

using namespace std;

typedef long long int LLI;

struct patient {
	LLI v, d, p;
	bool alive;
};

int main (void) {
	int n, treat = 0;
	cin >> n;
	struct patient patients[n];
	bool treatment[n];
	for (int i = 0; i < n; i++) {
		cin >> patients[i].v >> patients[i].d >> patients[i].p;
		patients[i].alive = true;
		treatment[i] = false;
	}
	for (int i = 0; i < n; i++) {
		if (!patients[i].alive) {
			continue;
		}
		treatment[i] = true;
		treat++;
		LLI curD = 0, curV = patients[i].v;
		for (int j = i+1; j < n; j++) {
			if (!patients[j].alive) {
				continue;
			}
			patients[j].p -= (curD + curV);
			if (patients[j].p < 0) {
				patients[j].alive = false;
				curD += patients[j].d;
			}
			if (curV > 0) {
				curV--;
			}
		}
	}
	cout << treat << endl;
	for (int i = 0; i < n; i++) {
		if (treatment[i]) {
			cout << i+1 << " ";
		}
	}
	cout << endl;
	return 0;
}
