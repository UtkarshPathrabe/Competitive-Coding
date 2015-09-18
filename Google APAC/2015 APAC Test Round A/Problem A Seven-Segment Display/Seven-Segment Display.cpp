#include <bits/stdc++.h>

using namespace std;

string original[10] = {"1111110", "0110000", "1101101", "1111001", "0110011", "1011011", "1011111", "1110000", "1111111", "1111011"};

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("A-large-practice.out");
	cin.open("A-large-practice.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, totalFail = 0;
		vector<string> str;
		vector<int> ans;
		cin >> N;
		for (int i = 0; i < N; i++) {
			string temp;
			cin >> temp;
			str.push_back(temp); 
		}
		for (int begin = 0; begin < 10; begin++) {
			vector<int> pos;
			pos.resize(7);
			int fail = 0;
			for (int i = 0; (i < N) && (!fail); i++) {
				int num = ((begin-i)%10 + 10)%10;
				for (int j = 0; j < 7; j++) {
					if (str[i][j] == '1') {
						if (original[num][j] == '1') {
							if (pos[j] == 0) {
								pos[j] = 1;
							} else if (pos[j] == 2) {
								fail = 1;
								break;
							}
						} else {
							fail = 1;
							break;
						}
					} else {
						if (original[num][j] == '1') {
							if (pos[j] == 1) {
								fail = 1;
								break;
							} else  {
								pos[j] = 2;
							}
						}
					}
				}
			}
			int num = ((begin-N)%10 + 10)%10;
			if (!fail) {
				vector <int> temp;
				temp.resize(7);
				for (int j = 0; j < 7; j++) {
					if (original[num][j] == '1') {
						if (pos[j] == 0) {
							totalFail = 1;
						} else if (pos[j] == 1) {
							temp[j] = 1;
						}
					}
				}
				if (ans.size() == 0 || ans == temp) {
					ans = temp;
				} else {
					totalFail = 1;
				}
			}
		}
		if (ans.size() == 0) {
			totalFail = 1;
		}
		cout << "Case #" << t << ": ";
		if (totalFail) {
			cout << "ERROR!" << endl;
		} else {
			for (int i = 0; i < 7; i++) {
				cout << ans[i];
			}
			cout << endl;
		}
	}
	cout.close();
	cin.close();
	return 0;
}
