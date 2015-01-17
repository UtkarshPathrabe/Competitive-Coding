/* Author: Utkarsh Pathrabe
*  Algorithm: Breadth First Search Traversal of Graphs
*/

/* The operations of enqueuing and dequeuing take O(1) time, so the total time devoted to queue
*  operations is O(V). Because the adjacency list of each vertex is scanned only when the vertex
*  is dequeued, each adjacency list is scanned at most once. Since the sum of the lengths of all
*  the adjacency lists is Theta(E), the total time spent in scanning adjacency lists is O(E). The
*  overhead for initialization is O(V), and thus the total running time of BFS is O(V + E). Thus,
*  breadth-first search runs in time linear in the size of the adjacency-list representation of G.
*/

#include <bits/stdc++.h>

using namespace std;

struct Edges{
	int to;
	int nextID;
};
typedef struct Edges edge;

struct Nodes{
	bool visited;
	int distance;
	int parent;
	int lastID;
};
typedef struct Nodes node;
	
vector <node> Node;
vector <edge> Edge;

int n;

void BFS (int x) {
	list<int> queue;
	Node[0].visited = true;
	for (int i = 1; i <= n; i++) {
		Node[i].visited = false;
		Node[i].distance = INT_MIN;
		Node[i].parent = INT_MIN;
	}
	cout << "The Breadth First Search Traversal of the Graph starting from node " << x << " gives:" << endl;
	Node[x].visited = true;
	Node[x].distance = 0;
	Node[x].parent = 0;
	queue.push_back(x);
	while (!queue.empty()) {
		x = queue.front();
		cout << x << "(" << Node[x].distance << ", " << Node[x].parent << ")" << "\t";
		queue.pop_front();
		for (int ID = Node[x].lastID; ID != -1; ID = Edge[ID].nextID) {
			if (!Node[Edge[ID].to].visited) {
				Node[Edge[ID].to].visited = true;
				Node[Edge[ID].to].distance = Node[x].distance + 1;
				Node[Edge[ID].to].parent = x;
				queue.push_back(Edge[ID].to);
			}
		}
	}
	cout << endl;
}

/* The following procedure prints out the vertices on a shortest path from s to v, assuming that
*  BFS has already been run to compute the shortest-path tree. 
*/
void PrintPath (vector<node> &Node, int s, int v) {
	if (v == s) {
		cout << s << "\t";
	} else if (Node[v].parent == INT_MIN) {
		cout << "No path from " << s << " to " << v << " exists." << endl;
	} else {
		PrintPath (Node, s, Node[v].parent);
		cout << v << "\t";
	}
}

int main (void) {
	int from, to, ID;
	edge e;
	node nod;
	char c;
	cout << "Which type of graph you want to enter? (Type 'd' for directed graph and 'u' for undirected graph):" << endl;
	cin >> c;
	cout << "Enter the number of nodes in the graph:" << endl;
	cin >> n;
	for (int i = 0; i <= n; i++) {
		nod.visited = false;
		nod.distance = INT_MIN;
		nod.parent = INT_MIN;
		nod.lastID = -1;
		Node.push_back(nod);
	}
	e.to = -1;
	e.nextID = -1;
	Edge.push_back(e);
	ID = 1;
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number) in each line(Write '-1 -1' if the list of edges is over):" << endl;
	cin >> from >> to;
	do{
		if (c == 'd') {
			e.to = to;
			e.nextID = Node[from].lastID;
			Edge.push_back(e);
			Node[from].lastID = ID;
			ID += 1;
		} else {
			e.to = to;
			e.nextID = Node[from].lastID;
			Edge.push_back(e);
			Node[from].lastID = ID;
			ID += 1;
			e.to = from;
			e.nextID = Node[to].lastID;
			Edge.push_back(e);
			Node[to].lastID = ID;
			ID += 1;
		}
		cin >> from >> to;
	}while(from != -1);
	cout << "From which node do you want to start the search:" << endl;
	cin >> from;
	BFS(from);
	cout << "To which node do you want to find the shortest path starting from " << from << ":" << endl;
	cin >> to;
	PrintPath(Node, from, to);
	cout << endl;
	Node.erase(Node.begin(), Node.end());
	Edge.erase(Edge.begin(), Edge.end());
	return 0;
}
