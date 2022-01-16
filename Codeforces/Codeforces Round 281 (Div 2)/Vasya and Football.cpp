/* Author: Utkarsh Pathrabe
*  Question can be found at http://codeforces.com/contest/493/problem/A 
*  Algorithms: Implementation
*/

#include <bits/stdc++.h>

using namespace std;

int main(void) {
	char home[21], away[21];
	int n, playerHome[100] = {0}, playerAway[100] = {0}, time, player;
	char team, card;
	cin >> home >> away >> n;
	for(int i = 0; i < n; i++) {
		cin >> time >> team >> player >> card;
		if(team == 'h') {
			if((card == 'r') && (playerHome[player] != 2)) {
				cout << home << ' ' << player << ' ' << time << endl;
				playerHome[player] = 2;
			}else if((card == 'y') && (playerHome[player] == 1)) {
				cout << home << ' ' << player << ' ' << time << endl;
				playerHome[player] = 2;
			}else if((card == 'y') && (playerHome[player] != 2)) {
				playerHome[player] = 1;
			}
		}else{
			if((card == 'r') && (playerAway[player] != 2)) {
				cout << away << ' ' << player << ' ' << time << endl;
				playerAway[player] = 2;
			}else if((card == 'y') && (playerAway[player] == 1)) {
				cout << away << ' ' << player << ' ' << time << endl;
				playerAway[player] = 2;
			}else if((card == 'y') && (playerAway[player] != 2)) {
				playerAway[player] = 1;
			}
		}
	}
	return 0;
}
