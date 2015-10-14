#include <bits/stdc++.h>

using namespace std;

const double pi = atan (1.0) * 4;

int main (void) {
	ifstream cin;
	cin.open("B-small-practice.in");
	FILE *fp;
	fp = fopen ("B-small-practice.out", "w");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		double V, D;
		cin >> V >> D;
		double tmp = D * 9.8 / (V * V);
		if (tmp > 1) {
			tmp = 1;
		} else if (tmp < 0) {
			tmp = 0;
		}
		double ans = asin (tmp) * 180.0 / pi / 2.0;
		fprintf(fp, "Case #%d: %.6f\n", t, ans);
	}
	cin.close();
	fclose(fp);
	return 0;
}
