/* Author: Utkarsh Pathrabe
*  Algorithm: Depth First Search Traversal of Graphs
*/

/* The running time of DFS is Theta(V + E). */

#include <bits/stdc++.h>

using namespace std;

struct Edges{
	int to;
	int nextID;
	char type;				//'t' for tree edge, 'b' for back edge, 'f' for forward edge, 'c' for cross edge and 'u' for unknown
};
typedef struct Edges edge;

struct Nodes{
	char color;				//'w' for white(undiscovered vertex), 'g' for gray(discovered but not finished vertex) and 'b' for black(finished vertex)
	int distance;
	int parent;
	int discover;
	int finish;
	int lastID;
};
typedef struct Nodes node;
	
vector <node> Node;
vector <edge> Edge;

list <int> Stack;

int n, m, timer;
char c;

void DFSUtility (int x, vector<node> &Node) {
	Node[x].color = 'g';
	Node[x].discover = ++timer;
	cout << x << "(" << Node[x].distance << ", " << Node[x].parent << ")" << "\t";
	for (int ID = Node[x].lastID; ID != -1; ID = Edge[ID].nextID) {
		if (Node[Edge[ID].to].color == 'w') {
			Node[Edge[ID].to].distance = Node[x].distance + 1;
			Node[Edge[ID].to].parent = x;
			Edge[ID].type = 't';
			DFSUtility(Edge[ID].to, Node);
		} else if (Node[Edge[ID].to].color == 'g') {
			Edge[ID].type = 'b';
		} else if (c == 'd'){
			if (Node[x].discover < Node[Edge[ID].to].discover) {
				Edge[ID].type = 'f';
			} else if (Node[x].discover > Node[Edge[ID].to].discover) {
				Edge[ID].type = 'c';
			}
		}
	}
	Node[x].color = 'b';
	Node[x].finish = ++timer;
	Stack.push_back(x);
}

void DFS (int x) {
	Node[0].color = 'b';
	for (int i = 1; i <= n; i++) {
		Node[i].color = 'w';
		Node[i].distance = INT_MIN;
		Node[i].parent = INT_MIN;
		Node[i].discover = INT_MIN;
		Node[i].finish = INT_MIN;
	}
	timer = 0;
	cout << "The Depth First Search Traversal of the Graph starting from node " << x << " gives:" << endl;
	Node[x].distance = 0;
	Node[x].parent = 0;
	DFSUtility(x, Node);
	for (int i = 1; i <= n; i++) {
		if (Node[i].color == 'w') {
			Node[i].distance = 0;
			Node[i].parent = 0;
			DFSUtility(i, Node);
		}
	}
	cout << endl;
}

/* Topological sort can be performed in time Theta(V + E), since depth-first search takes Theta(V + E)
*  time and it takes O(1) time to insert each of the |V| vertices onto the front of the linked list.
*/
void TopologicalSort (int x) {
	if ((c == 'd') && (m <= n)) {
		DFS(x);
		cout << "Topological Sort gives:" << endl;
		for (int i = 0; i < n; i++) {
			cout << Stack.back() << "\t";
			Stack.pop_back();
		}
		cout << endl;
	} else {
		if (c != 'd') {
			cout << "Topological Sort cannot be performed as it is an undirected graph." << endl;
		} else {
			cout << "Topological Sort cannot be performed as the graph has cycles." << endl;
		}
	}
}

int main (void) {
	int from, to, ID;
	edge e;
	node nod;
	char response = 'y';
	cout << "Which type of graph you want to enter? (Type 'd' for directed graph and 'u' for undirected graph):" << endl;
	cin >> c;
	cout << "Enter the number of nodes in the graph:" << endl;
	cin >> n;
	for (int i = 0; i <= n; i++) {
		nod.color = 'w';
		nod.distance = INT_MIN;
		nod.parent = INT_MIN;
		nod.discover = INT_MIN;
		nod.finish = INT_MIN;
		nod.lastID = -1;
		Node.push_back(nod);
	}
	e.to = -1;
	e.nextID = -1;
	e.type = 'u';
	Edge.push_back(e);
	ID = 1;
	cout << "Enter the edges in the format(From Node Number <Space> To Node Number) in each line(Write '-1 -1' if the list of edges is over):" << endl;
	cin >> from >> to;
	do{
		if (c == 'd') {
			e.to = to;
			e.nextID = Node[from].lastID;
			e.type = 'u';
			Edge.push_back(e);
			Node[from].lastID = ID;
			ID += 1;
		} else {
			e.to = to;
			e.nextID = Node[from].lastID;
			e.type = 'u';
			Edge.push_back(e);
			Node[from].lastID = ID;
			ID += 1;
			e.to = from;
			e.nextID = Node[to].lastID;
			e.type = 'u';
			Edge.push_back(e);
			Node[to].lastID = ID;
			ID += 1;
		}
		cin >> from >> to;
	}while(from != -1);
	cout << "From which node do you want to start the search:" << endl;
	cin >> from;
	DFS(from);
	cout << "Do you want me to print out contents of Node and Edge Entries:" << endl;
	cin >> response;
	if (response == 'y') {
		cout << "The Node entries are: " << endl;
		cout << "Node\tColor\tDistance\tParent\tDiscover\tFinish\tLast Edge ID" << endl;
		for (int i = 1; i <= n; i++) {
			cout << i << "\t" << Node[i].color << "\t" << Node[i].distance << "\t\t" << Node[i].parent << "\t" << Node[i].discover << "\t\t" << Node[i].finish << "\t" << Node[i].lastID << endl;
		}
		cout << "The Edge entries are: " << endl;
		cout << "ID\tTo\tType\tNext Egde ID" << endl;
		m = (Edge.end() - Edge.begin());
		if (c != 'd') {
			for (int i = 1; i < m; i += 2) {
				if (((Edge[i].type == 'b') && (Edge[i+1].type == 't')) || ((Edge[i].type == 't') && (Edge[i+1].type == 'b'))) {
					Edge[i].type = Edge[i+1].type = 't';
				} else if (((Edge[i].type == 'b') && (Edge[i+1].type == 'u')) || ((Edge[i].type == 'u') && (Edge[i+1].type == 'b'))) {
					Edge[i].type = Edge[i+1].type = 'b';
				}
			}
		}
		for (int i = 1; i < m; i++) {
			cout << i << "\t" << Edge[i].to << "\t" << Edge[i].type << "\t" << Edge[i].nextID << endl;
		}
	}
	if (c == 'd') {
		cout << "Do you want me to do topological sort on the given graph:" << endl;
		cin >> response;
		if (response == 'y') {
			TopologicalSort (from);
		}
	}
	return 0;
}
