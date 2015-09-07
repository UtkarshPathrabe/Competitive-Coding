#include <bits/stdc++.h>

using namespace std;

int findMin (vector<int> &dist, vector<bool> &flag) {
	int min = INT_MAX, minIndex = -1;
	for (int i = 0; i < dist.size(); i++) {
		if ((!flag[i]) && (min >= dist[i])) {
			min = dist[i];
			minIndex = i;
		}
	}
	return minIndex;
}

void dijkstra (vector< vector <int> > &graph, int src) {
	vector<int> dist;
	vector<bool> flag;
	for (int i = 0; i < graph.size(); i++) {
		dist.push_back(INT_MAX);
		flag.push_back(false);
	}
	dist[src] = 0;
	for (int i = 0; i < graph.size() - 1; i++) {
		int u = findMin (dist, flag);
		flag[u] = true;
		for (int v = 0; v < graph[u].size(); v++) {
			if ((!flag[v]) && (graph[u][v]) && (dist[u] != INT_MAX) && (dist[u] + graph[u][v] < dist[v])) {
				dist[v] = dist[u] + graph[u][v];
			}
		}
	}
	cout << "Distance to following destinations from source node " << src << " are:" << endl;
	for (int i = 0; i < graph.size(); i++) {
		cout << i << "\t:\t" << dist[i] << endl;
	}
}

int main (void) {
	vector < vector <int> > graph;
	vector <int> temp;
	temp.push_back (0);
	temp.push_back (4);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (8);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (4);
	temp.push_back (0);
	temp.push_back (8);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (11);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (8);
	temp.push_back (0);
	temp.push_back (7);
	temp.push_back (0);
	temp.push_back (4);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (2);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (7);
	temp.push_back (0);
	temp.push_back (9);
	temp.push_back (14);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (9);
	temp.push_back (0);
	temp.push_back (10);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (4);
	temp.push_back (0);
	temp.push_back (10);
	temp.push_back (0);
	temp.push_back (2);
	temp.push_back (0);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (14);
	temp.push_back (0);
	temp.push_back (2);
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (6);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (8);
	temp.push_back (11);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (1);
	temp.push_back (0);
	temp.push_back (7);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (2);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (0);
	temp.push_back (6);
	temp.push_back (7);
	temp.push_back (0);
	graph.push_back (temp);
	temp.erase (temp.begin(), temp.end());
	dijkstra (graph, 0);
	return 0;
}
