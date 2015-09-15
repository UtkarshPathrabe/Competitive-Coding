/* Time Complexity: O(E*(V^3)) [For BFS it is O(V^2), if adjacency list representation is used, then Time Complexity would be O(E*(V^2))] */

#include <bits/stdc++.h>

using namespace std;

bool BFS (vector< vector<int> > &resiGraph, int src, int sink, int parent[]) {
	int V = resiGraph.size();
	bool visited[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
	}
	queue<int> q;
	q.push(src);
	visited[src] = true;
	parent[src] = -1;
	while (!q.empty()) {
		int u = q.front();
		q.pop();
		for (int v = 0; v < V; v++) {
			if ((!visited[v]) && (resiGraph[u][v] > 0)) {
				q.push (v);
				visited[v] = true;
				parent[v] = u;
			}
		}
	}
	return (visited[sink] == true);
}

void DFS (vector< vector<int> > &resiGraph, int src, bool visited[]) {
	visited[src] = true;
	for (int dest = 0; dest < resiGraph.size(); dest++) {
		if ((resiGraph[src][dest]) && (!visited[dest])) {
			DFS (resiGraph, dest, visited);
		}
	}
}

void minCut (vector< vector<int> > &graph, int src, int sink) {
	int V = graph.size();
	vector< vector<int> > resiGraph;
	for (int i = 0; i < V; i++) {
		vector<int> temp;
		for (int j = 0; j < V; j++) {
			temp.push_back(graph[i][j]); 
		}
		resiGraph.push_back(temp);
		temp.erase(temp.begin(), temp.end());
	}
	int *parent = new int[V];
	while (BFS (resiGraph, src, sink, parent)) {
		int path_flow = INT_MAX;
		for (int v = sink; v != src; v = parent[v]) {
			int u = parent[v];
			path_flow = min (path_flow, resiGraph[u][v]);
		}
		for (int v = sink; v != src; v = parent[v]) {
			int u = parent[v];
			resiGraph[u][v] -= path_flow;
			resiGraph[v][u] += path_flow;
		}
		
	}
	bool visited[V];
	memset (visited, false, sizeof (visited));
	DFS (resiGraph, src, visited);
	for (int u = 0; u < V; u++) {
		for (int v = 0; v < V; v++) {
			if ((visited[u]) && (!visited[v]) && (graph[u][v])) {
				cout << u << "\t->\t" << v << endl;
			}
		}
	}
}

int main (void) {
	vector< vector<int> > graph;
	vector<int> temp;
	temp.push_back(0);
	temp.push_back(16);
	temp.push_back(13);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(10);
	temp.push_back(12);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(4);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(14);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(9);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(20);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(7);
	temp.push_back(0);
	temp.push_back(4);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	temp.push_back(0);
	graph.push_back(temp);
	temp.erase(temp.begin(), temp.end());
	cout << "The Edges in the Minimum Cut are:" << endl;
	cout << "Source\t\tDestination" << endl;
	minCut (graph, 0, 4);
	return 0;
}
