#include <bits/stdc++.h>

using namespace std;

struct qEntry {
	int v, dist;
};

int minDiceThrows (vector <int> &move) {
	int N = move.size();
	bool* visited = new bool[N];
	for (int i = 0; i < N; i++) {
		visited[i] = false;
	}
	queue<qEntry> q;
	qEntry a = {0, 0}, b;
	q.push (a);
	while (!q.empty()) {
		b = q.front();
		int v = b.v;
		if (v == N-1) {
			break;
		}
		q.pop();
		for (int i = (b.v + 1); i <= (b.v + 6) && i < N; i++) {
			if (!visited[i]) {
				visited[i] = true;
				qEntry c;
				c.dist = b.dist + 1;
				if (move[i] != -1) {
					c.v = move[i];
				} else {
					c.v = i;
				}
				q.push(c);
			}
		}
	}
	return b.dist;
}

int main (void) {
	vector<int> moves;
	int N = 30;
	for (int i = 0; i < N; i++) {
		moves.push_back(-1);
	}
	//Ladders
	moves[2] = 21;
	moves[4] = 7;
    moves[10] = 25;
    moves[19] = 28;
    //Snakes
    moves[26] = 0;
    moves[20] = 8;
    moves[16] = 3;
    moves[18] = 6;
    cout << "Minimum Number of dice throws required is " << minDiceThrows(moves) << "." << endl;
	return 0;
}
