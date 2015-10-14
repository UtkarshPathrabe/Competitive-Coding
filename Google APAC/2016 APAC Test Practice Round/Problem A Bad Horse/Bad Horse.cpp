#include <bits/stdc++.h>

using namespace std;

bool isBipartite (vector< vector<int> > &G, int src) {
	int V = G.size();
	int color[V];
	for (int i = 0; i < V; i++) {
		color[i] = -1;
	}
	color[src] = 1;
	queue<int> Q;
	Q.push(src);
	while (!Q.empty()) {
		int u = Q.front();
		Q.pop();
		for (int v = 0; v < V; v++) {
			if ((G[u][v]) && (color[v] == -1)) {
				color[v] = 1 - color[u];
				Q.push(v);
			} else if ((G[u][v]) && (color[u] == color[v])) {
				return false;
			}
		}
	}
	return true;
}

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("A-small-practice-2.out");
	cin.open("A-small-practice-2.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int M;
		cin >> M;
		vector< pair<string, string> > data;
		map<string, int> index;
		vector< vector<int> > graph;
		for (int i = 0, count = 0; i < M; i++) {
			string temp1, temp2;
			cin >> temp1 >> temp2;
			data.push_back(make_pair(temp1, temp2));
			if (index.find(temp1) == index.end()) {
				index.insert(make_pair(temp1, count++));
			}
			if (index.find(temp2) == index.end()) {
				index.insert(make_pair(temp2, count++));
			}
		}
		int V = index.size();
		for (int i = 0; i < V; i++) {
			vector<int> temp(V, 0);
			graph.push_back(temp);
		}
		for (int i = 0; i < M; i++) {
			map<string, int>::iterator it1 = index.find(data[i].first);
			map<string, int>::iterator it2 = index.find(data[i].second);
			graph[it1->second][it2->second] = 1;
			graph[it2->second][it1->second] = 1;
		}
		cout << "Case #" << t << ": ";
		isBipartite (graph, 0) ? cout << "Yes" << endl : cout << "No" << endl;
	}
	cout.close();
	cin.close();
	return 0;
}
