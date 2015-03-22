#include <bits/stdc++.h>

using namespace std;

vector<string> strVector;

int main(void) {
	int T;
	cin >> T;
	while (T--) {
		int N;
		cin >> N;
		string str;
		cin >> str;
		for (int i = 1; i < (1 << N); i++) {
			string ans = "";
			for (int j = 0; j < N; j++)
				if (i & (1 << j))
					ans += str[j];
			strVector.push_back(ans);
		}
		sort(strVector.begin(), strVector.end());
		for (int i = 0; i < (1 << N) - 1; i++)
			cout << strVector[i] << endl;
		strVector.clear ();
	}
	return 0;
}
