/* Author: Utkarsh Pathrabe
*  Algorithm: Kruskals Minimum Spanning Tree Algorithm
*/

/* MST-KRUSKAL(G, w):
*	1 A <- Empty
*	2 for each vertex v belonging to V[G]
*	3 		do MAKE-SET(v)
*	4 sort the edges of E into nondecreasing order by weight w
*	5 for each edge (u, v) belonging to E, taken in nondecreasing order by weight
*	6 		do if FIND-SET(u) not equal to FIND-SET(v)
*	7 			then A <- A union {(u, v)}
*	8 				 UNION(u, v)
*	9 return A
*/

/* Time Complexity: O(E*log(E)) or O(E*log(V)). Sorting of edges takes O(E*log(E)) time. After sorting, we iterate through all edges and apply find-union algorithm.
*  The Find and Union operations can take atmost O(log(V)) time. So, overall complexity is O(E*log(E) + E*log(V)) time. The value of E can be atmost V^2, so O(log(V)) are O(log(E)) same.
*  Therefore, overall time complexity is O(E*log(E)) or O(E*log(V)).
*/

#include <bits/stdc++.h>

using namespace std;

struct Edges{											//Represents weighted edge in graph
	int source;
	int destination;
	int weight;
};
typedef struct Edges edge;

struct Nodes{											//Structure to represent a subset for Union-Find
	int parent;
	int rank;
};
typedef struct Nodes node;

vector <node> Node;
vector <edge> Edge;

int V, E;

bool myComparator (const Edges &a, const Edges &b) {	//Compare two edges according to their weights
	return ((a.weight) < (b.weight));
}

int Find (int x) {										//A utility function to find set of an element x, using the Path-Compression Technique
	if (Node[x].parent != x) {
		Node[x].parent = Find(Node[x].parent);
	}
	return Node[x].parent;
}

int Union (int x, int y) {								//A utility function that does the Union of two sets x and y, using Union-By-Rank
	int xRoot = Find(x);
	int yRoot = Find(y);
	if (Node[xRoot].rank < Node[yRoot].rank) {
		Node[xRoot].parent = yRoot;
	} else if (Node[xRoot].rank > Node[yRoot].rank) {
		Node[yRoot].parent = xRoot;
	} else {
		Node[yRoot].parent = xRoot;
		Node[xRoot].rank += 1;
	}
}

void Kruskal () {
	int e = 0, i = 0, x, y;
	edge ed;
	vector <edge> Result;
	sort(Edge.begin(), Edge.end(), myComparator);
	cout << "The Minimum Spanning Tree for the given graph is:" << endl;
	while (e < (V - 1)) {
		ed = Edge[i++];
		x = Find (ed.source);
		y = Find (ed.destination);
		if (x != y) {
			Union (x, y);
			cout << ed.source << "\t" << ed.destination << "\t" << ed.weight << endl;
			Result.push_back(ed);
			e += 1;
		}
	}
}

int main (void) {
	node nod;
	edge e;
	cout << "Enter number of vertices in the graph:" << endl;
	cin >> V;
	for (int i = 0; i <= V; i++) {
		nod.parent = i;
		nod.rank = 0;
		Node.push_back(nod);
	}
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number <Space> Weight of Edge) in each line(Write '-1 -1 -1' if the list of edges is over):" << endl;
	cin >> e.source >> e.destination >> e.weight;
	do{
		Edge.push_back(e);
		cin >> e.source >> e.destination >> e.weight;
	}while(e.source != -1);
	E = Edge.end() - Edge.begin();
	Kruskal();
	Node.erase(Node.begin(), Node.end());
	Edge.erase(Edge.begin(), Edge.end());
	return 0;
}
