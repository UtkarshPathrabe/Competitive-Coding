#include <bits/stdc++.h>

using namespace std;

int data[805][805] = {0};
int team[805] = {0};

int main (void) {
	int n;
	cin >> n;
	for (int i = 2; i <= (2*n); i++) {
		for (int j = 1; j < i; j++) {
			cin >> data[i][j];
		}
	}
	int teams = n;
	while (teams--) {
		int indexX = 0, indexY = 0, maxi = INT_MIN;
		for (int i = 2; i <= (2*n); i++) {
			for (int j = 1; j < i; j++) {
				if (data[i][j] > maxi) {
					maxi = data[i][j];
					indexX = i;
					indexY = j;
				}
			}
		}
		for (int i = 1; i <= (2*n); i++) {
			data[indexX][i] = 0;
			data[indexY][i] = 0;
			data[i][indexY] = 0;
			data[i][indexX] = 0;
		}
		team[indexX] = indexY;
		team[indexY] = indexX;
	}
	for (int i = 1; i <= (2*n); i++) {
		cout << team[i];
		if (i == 2*n) {
			cout << endl;
		} else {
			cout << " ";
		}
	}
	return 0;
}
