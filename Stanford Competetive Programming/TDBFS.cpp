#include <bits/stdc++.h>

using namespace std;

struct Edges{
	int to;
	int nextID;
};
typedef struct Edges edge;

struct Nodes{
	bool visited;
	int lastID;
};
typedef struct Nodes node;

vector <node> Node;
vector <edge> Edge;

int t, n, m, ID;

void BFS (int x) {
	list<int> queue;
	Node[0].visited = true;
	for (int i = 1; i <= n; i++) {
		Node[i].visited = false;
	}
	Node[x].visited = true;
	queue.push_back(x);
	while (!queue.empty()) {
		x = queue.front();
		cout << x << " ";
		queue.pop_front();
		for (int ID = Node[x].lastID; ID != -1; ID = Edge[ID].nextID) {
			if (!Node[Edge[ID].to].visited) {
				Node[Edge[ID].to].visited = true;
				queue.push_back(Edge[ID].to);
			}
		}
	}
}

void DFSUtility (int x, vector<node> &Node) {
	Node[x].visited = true;
	cout << x << " ";
	for (int ID = Node[x].lastID; ID != -1; ID = Edge[ID].nextID) {
		if (Node[Edge[ID].to].visited == false) {
			DFSUtility(Edge[ID].to, Node);
		}
	}
}

void DFS (int x) {
	Node[0].visited = true;
	for (int i = 1; i <= n; i++) {
		Node[i].visited = false;
	}
	DFSUtility(x, Node);
}

int main (void) {
	int from, to, v, type, cas = 1;
	node nod;
	edge e;
	cin >> t;
	while (t--) {
		cin >> n;
		e.to = -1;
		e.nextID = -1;
		Edge.push_back(e);
		ID = 1;
		for (int i = 0; i <= n; i++) {
			nod.visited = false;
			nod.lastID = -1;
			Node.push_back (nod);
		}
		for (int i = 1; i <= n; i++) {
			cin >> from >> m;
			while (m--) {
				cin >> to;
				e.to = to;
				e.nextID = Node[from].lastID;
				Edge.push_back(e);
				Node[from].lastID = ID;
				ID += 1;
			}
		}
		cin >> v >> type;
		cout << "graph " << cas << endl;
		cas += 1;
		while (v != 0) {
			if (type == 0) {
				DFS (v);
				cout << endl;
			} else {
				BFS (v);
				cout << endl;
			}
			cin >> v >> type;
		}
	}
	return 0;
}
