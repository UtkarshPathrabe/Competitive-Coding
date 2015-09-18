/* @Author: Utkarsh Ashok Pathrabe */

#include <bits/stdc++.h>

using namespace std;

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("B-large-practice.out");
	cin.open("B-large-practice.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		string dir;
		cin >> N >> dir;
		vector < vector <int> > board;
		vector <int> temp;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int a;
				cin >> a;
				temp.push_back(a);
			}
			board.push_back (temp);
			temp.erase (temp.begin(), temp.end());
		}
		if (dir.compare("right") == 0) {
			for (int i = 0; i < N; i++) {
				for (int j = N-1, k = N-2; ((j >= 0) && (k >= 0)); ) {
					if (board[i][j] == board[i][k]) {
						board[i][j] += board[i][k];
						board[i][k] = 0;
						j = k-1;
						k = j-1;
					} else {
						if (board[i][k] == 0) {
							k--;
						} else {
							j = k;
							k--;
						}
					}
				}
				for (int j = N-1; j >= 0; j--) {
					if (board[i][j] == 0) {
						for (int k = j - 1; k >= 0; k--) {
							if (board[i][k] != 0) {
								board[i][j] = board[i][k];
								board[i][k] = 0;
								break;
							}
						}
					}
					if (board[i][j] == 0) {
						break;
					}
				}
			}
		} else if (dir.compare("left") == 0) {
			for (int i = 0; i < N; i++) {
				for (int j = 0, k = 1; ((j < N) && (k < N)); ) {
					if (board[i][j] == board[i][k]) {
						board[i][j] += board[i][k];
						board[i][k] = 0;
						j = k+1;
						k = j+1;
					} else {
						if (board[i][k] == 0) {
							k++;
						} else {
							j = k;
							k++;
						}
					}
				}
				for (int j = 0; j < N; j++) {
					if (board[i][j] == 0) {
						for (int k = j + 1; k < N; k++) {
							if (board[i][k] != 0) {
								board[i][j] = board[i][k];
								board[i][k] = 0;
								break;
							}
						}
					}
					if (board[i][j] == 0) {
						break;
					}
				}
			}
		} else if (dir.compare("up") == 0) {
			for (int j = 0; j < N; j++) {
				for (int i = 0, k = 1; ((i < N) && (k < N)); ) {
					if (board[i][j] == board[k][j]) {
						board[i][j] += board[k][j];
						board[k][j] = 0;
						i = k+1;
						k = i+1;
					} else {
						if (board[k][j] == 0) {
							k++;
						} else {
							i = k;
							k++;
						}
					}
				}
				for (int i = 0; i < N; i++) {
					if (board[i][j] == 0) {
						for (int k = i + 1; k < N; k++) {
							if (board[k][j] != 0) {
								board[i][j] = board[k][j];
								board[k][j] = 0;
								break;
							}
						}
					}
					if (board[i][j] == 0) {
						break;
					}
				}
			}
		} else if (dir.compare("down") == 0) {
			for (int j = 0; j < N; j++) {
				for (int i = N-1, k = N-2; ((i >= 0) && (k >= 0)); ) {
					if (board[i][j] == board[k][j]) {
						board[i][j] += board[k][j];
						board[k][j] = 0;
						i = k-1;
						k = i-1;
					} else {
						if (board[k][j] == 0) {
							k--;
						} else {
							i = k;
							k--;
						}
					}
				}
				for (int i = N-1; i >= 0; i--) {
					if (board[i][j] == 0) {
						for (int k = i - 1; k >= 0; k--) {
							if (board[k][j] != 0) {
								board[i][j] = board[k][j];
								board[k][j] = 0;
								break;
							}
						}
					}
					if (board[i][j] == 0) {
						break;
					}
				}
			}
		}
		cout << "Case #" << t << ":" << endl;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cout << board[i][j] << " ";
			}
			cout << endl;
		}
	}
	cout.close();
	cin.close();
	return 0;
}
