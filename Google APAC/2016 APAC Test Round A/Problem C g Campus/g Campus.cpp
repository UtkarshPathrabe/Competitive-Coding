#include <bits/stdc++.h>

using namespace std;

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("C-large-practice.out");
	cin.open("C-large-practice.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, M;
		vector < vector<int> > graph;
		vector <int> temp;
		vector < pair < pair <int, int>, int > > E;
		cin >> N >> M;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) {
					temp.push_back (0);
				} else {
					temp.push_back (INT_MAX);
				}
			}
			graph.push_back(temp);
			temp.erase(temp.begin(), temp.end());
		}
		for (int i = 0; i < M; i++) {
			int U, V, C;
			cin >> U >> V >> C;
			E.push_back(make_pair(make_pair(U, V), C));
			graph[U][V] = min (graph[U][V], C);
			graph[V][U] = min (graph[V][U], C);
		}
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if ((graph[i][k] != INT_MAX) && (graph[k][j] != INT_MAX) && (graph[i][k] + graph[k][j] < graph[i][j]))
						graph[i][j] = graph[i][k] + graph[k][j];
				}
			}
		}
		cout << "Case #" << t << ":" << endl;
		for (int k = 0; k < M; k++) {
			int U = E[k].first.first;
			int V = E[k].first.second;
			int C = E[k].second;
			bool flag = false;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (graph[i][U] + C + graph[V][j] == graph[i][j]) {
						flag = true;
						break;
					}
				}
				if (flag) {
					break;
				}
			}
			if (!flag) {
				cout << k << endl;
			}
		}
	}
	cout.close();
	cin.close();
	return 0;
}
