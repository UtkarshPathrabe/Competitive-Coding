#include <bits/stdc++.h>

using namespace std;

int main (void) {
	FILE *fp;
	ifstream cin;
	cin.open("B-large-practice.in");
	fp = fopen ("B-large-practice.out", "w+");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, M;
		cin >> N >> M;
		vector<double> a;
		for (int i = 0; i < N; i++) {
			int temp;
			cin >> temp;
			a.push_back(log10(temp));
		}
		fprintf (fp, "Case #%d:\n", t);
		for (int i = 0; i < M; i++) {
			int L, R;
			double vol = 0;
			cin >> L >> R;
			for (int j = L; j <= R; j++) {
				vol += a[j];
			}
			vol /= (R-L+1);
			fprintf (fp, "%.12lf\n", pow(10, vol));
		}
	}
	cin.close();
	fclose(fp);
	return 0;
}
