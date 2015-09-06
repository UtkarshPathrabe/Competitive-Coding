#include <bits/stdc++.h>

using namespace std;

struct Edge {
	int src, dest, weight;
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

struct subset {
	int parent;
	int rank;
};

int find (struct subset s[], int i) {
	if (s[i].parent != i) {
		s[i].parent = find (s, s[i].parent);
	}
	return s[i].parent;
}

void Union (struct subset s[], int x, int y) {
	int xRoot = find (s, x);
	int yRoot = find (s, y);
	if (s[xRoot].rank < s[yRoot].rank) {
		s[xRoot].parent = yRoot;
	} else if (s[xRoot].rank > s[yRoot].rank) {
		s[yRoot].parent = xRoot;
	} else {
		s[yRoot].parent = xRoot;
		s[xRoot].rank++;
	}
}

void boruvkaMST (struct Graph *graph) {
	int V = graph->V;
	int E = graph->E;
	struct Edge* edge = graph->edge;
	struct subset *s = new subset[V];
	int *cheapest = new int[V];
	int numTrees = V;
	int MSTweight = 0;
	for (int v = 0; v < V; v++) {
		s[v].parent = v;
		s[v].rank = 0;
	}
	while (numTrees > 1) {
		for (int v = 0; v < V; v++) {
			cheapest[v] = -1;
		}
		for (int e = 0; e < E; e++) {
			int set1 = find (s, edge[e].src);
			int set2 = find (s, edge[e].dest);
			if (set1 == set2) {
				continue;
			} else {
				if ((cheapest[set1] == -1) || (edge[cheapest[set1]].weight > edge[e].weight)) {
					cheapest[set1] = e;
				}
				if ((cheapest[set2] == -1) || (edge[cheapest[set2]].weight > edge[e].weight)) {
					cheapest[set2] = e;
				}
			}
		}
		for (int v = 0; v < V; v++) {
			if (cheapest[v] != -1) {
				int set1 = find (s, edge[cheapest[v]].src);
				int set2 = find (s, edge[cheapest[v]].dest);
				if (set1 == set2) {
					continue;
				}
				MSTweight += edge[cheapest[v]].weight;
				cout << "Edge " << edge[cheapest[v]].src << "-" << edge[cheapest[v]].dest << ":\t" << edge[cheapest[v]].weight << " included in MST." << endl;
				Union (s, set1, set2);
				numTrees--;
			}
		}
	}
	cout << "Weight of MST is " << MSTweight << "." << endl;
	return;
}

int main (void) {
	int V = 4;  // Number of vertices in graph
    int E = 5;  // Number of edges in graph
	struct Graph* graph = createGraph(V, E);
    // add edge 0-1
    graph->edge[0].src = 0;
    graph->edge[0].dest = 1;
    graph->edge[0].weight = 10;
    // add edge 0-2
    graph->edge[1].src = 0;
    graph->edge[1].dest = 2;
    graph->edge[1].weight = 6;
    // add edge 0-3
    graph->edge[2].src = 0;
    graph->edge[2].dest = 3;
    graph->edge[2].weight = 5;
    // add edge 1-3
    graph->edge[3].src = 1;
    graph->edge[3].dest = 3;
    graph->edge[3].weight = 15;
    // add edge 2-3
    graph->edge[4].src = 2;
    graph->edge[4].dest = 3;
    graph->edge[4].weight = 4;
    boruvkaMST(graph);
	return 0;
}
