#include <bits/stdc++.h>

using namespace std;

class Graph {
	int V;
	list<int> *adj;
	public:
		Graph (int V);
		void addEdge (int u, int v);
		bool isReachable (int src, int dest);
};

Graph::Graph (int V) {
	this->V = V;
	adj = new list<int>[V];
}

void Graph::addEdge (int u, int v) {
	adj[u].push_back (v);
}

bool Graph::isReachable (int src, int dest) {
	if (src == dest) {
		return true;
	}
	bool *visited = new bool[V];
	for (int i = 0; i < V; i++) {
		visited[i] = false;
	}
	queue<int> q;
	list<int>::iterator i;
	visited[src] = true;
	q.push(src);
	while (!q.empty()) {
		int u = q.front();
		q.pop();
		for (i = adj[u].begin(); i != adj[u].end(); i++) {
			if (*i == dest) {
				return true;
			}
			if (!visited[*i]) {
				visited[*i] = true;
				q.push(*i);
			}
		}
	}
	return false;
}

int main (void) {
	Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
	g.addEdge(3, 3);
    int u = 1, v = 3;
	if(g.isReachable(u, v))
		cout<< "There is a path from " << u << " to " << v << "." << endl;
    else
        cout<< "There is no path from " << u << " to " << v << "." << endl;
    u = 3;
	v = 1;
    if(g.isReachable(u, v))
        cout<< "There is a path from " << u << " to " << v << "." << endl;
    else
        cout<< "There is no path from " << u << " to " << v << "." << endl;
	return 0;
}
