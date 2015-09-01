/* Time Complexity: O(E*log(V)) */

#include <bits/stdc++.h>

using namespace std;

struct Edge {
	int src, dest;
};

struct Graph {
	int V, E;
	struct Edge* edge;
};

struct Graph* createGraph (int V, int E) {
	struct Graph* graph = (struct Graph*) malloc (sizeof (struct Graph));
	graph->V = V;
	graph->E = E;
	graph->edge = (struct Edge*) malloc (E * sizeof (struct Edge));
	return graph;
}

void addEdge (struct Graph* graph, int src, int dest, int edgeNo) {
	graph->edge[edgeNo].src = src;
	graph->edge[edgeNo].dest = dest;
}

struct subset {
	int parent;
	int rank;
};

int Find (struct subset subSet[], int i) {
	if (subSet[i].parent != i) {
		subSet[i].parent = Find (subSet, subSet[i].parent);
	}
	return subSet[i].parent;
}

void Union (struct subset subSet[], int u, int v) {
	int uRoot = Find (subSet, u);
	int vRoot = Find (subSet, v);
	if (subSet[uRoot].rank < subSet[vRoot].rank) {
		subSet[uRoot].parent = vRoot;
	} else if (subSet[uRoot].rank > subSet[vRoot].rank) {
		subSet[vRoot].parent = uRoot;
	} else {
		subSet[vRoot].parent = uRoot;
		subSet[uRoot].rank++;
	}
}

bool isCyclic (struct Graph* graph) {
	struct subset *subSet = (struct subset*) malloc (graph->V * sizeof(struct subset));
	for (int i = 0; i < graph->V; i++) {
		subSet[i].parent = i;
		subSet[i].rank = 0;
	}
	for (int i = 0; i < graph->E; i++) {
		int x = Find (subSet, graph->edge[i].src);
		int y = Find (subSet, graph->edge[i].dest);
		if (x == y) {
			return true;
		}
		Union (subSet, x, y);
	}
	return false;
}

int main (void) {
	struct Graph* graph = createGraph (3, 3);
	addEdge (graph, 0, 1, 0);
	addEdge (graph, 1, 2, 1);
	addEdge (graph, 0, 2, 2);
	isCyclic (graph) ? cout << "Graph contains cycle." << endl : cout << "Graph does not contains cycle." << endl;
	return 0;
}
