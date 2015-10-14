#include <bits/stdc++.h>

using namespace std;

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("D-large-practice.out");
	cin.open("D-large-practice.in");
	int T, totalTime = 1100000;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int S, R, C;
		vector<int> X(totalTime+5, 0);
		cin >> S >> R >> C;
		for (int i = 1; i <= S; i++) {
			int time;
			char turn;
			cin >> time >> turn;
			if (turn == 'R') {
				X[time] = 1;
			} else {
				X[time] = -1;
			}
		}
		bool alright = true;
		int direction = 2;
		set< pair <int, int> > snake, food;
		deque < pair<int, int> > Q;
		snake.insert(make_pair(1, 1));
		Q.push_front(make_pair(1, 1));
		for (int i = 1; (i <= totalTime) && (alright); i++) {
			pair <int, int> head = Q.front();
			pair <int, int> to;
			if (direction == 1) {
				to = make_pair (head.first-1, head.second);
				if (to.first == 0) {
					to.first = R;
				}
			} else if (direction == 2) {
				to = make_pair (head.first, head.second+1);
				if (to.second == C+1) {
					to.second = 1;
				}
			} else if (direction == 3) {
				to = make_pair (head.first+1, head.second);
				if (to.first == R+1) {
					to.first = 1;
				}
			} else if (direction == 4) {
				to = make_pair (head.first, head.second-1);
				if (to.second == 0) {
					to.second = C;
				}
			}
			int x = to.first, y = to.second;
			if (((x+y)%2 == 1) && (food.find(to) == food.end())) {
				food.insert(to);
				if (snake.find(to) != snake.end()) {
					alright = false;
					break;
				}
				Q.push_front(to);
				snake.insert(to);
			} else {
				pair <int, int> tail = Q.back();
				if ((snake.find(to) != snake.end()) && (to != tail)) {
					alright = false;
					break;
				}
				snake.erase(tail);
				snake.insert(to);
				Q.pop_back();
				Q.push_front(to);
			}
			if (X[i] != 0) {
				direction += X[i];
				if (direction == 0) {
					direction = 4;
				}
				if (direction == 5) {
					direction = 1;
				}
			}
		}
		cout << "Case #" << t << ": " << Q.size() << endl;
	}
	cout.close();
	cin.close();
	return 0;
}
