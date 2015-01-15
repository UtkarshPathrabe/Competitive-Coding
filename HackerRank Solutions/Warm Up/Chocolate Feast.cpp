#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int T, N, C, M, choc, wrap;
	//ifstream in("ACMICPCTeam.txt");
	cin >> T;
	while (T--) {
		cin >> N >> C >> M;
		wrap = choc = N / C;
		while (wrap >= M) {
			choc += (wrap / M);
			wrap = (wrap / M) + (wrap % M);
		}
		cout << choc << endl;
	}
	return 0;
}
