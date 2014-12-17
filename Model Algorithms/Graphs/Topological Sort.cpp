/* Author: Utkarsh Pathrabe
*  Algorithm: Topological Sort
*/

/* Time complexity: Theta(V + E) */

#include <bits/stdc++.h>

using namespace std;

struct Edges{
	int to;
	int nextID;
};
typedef struct Edges edge;

struct Nodes{
	int inDegree;
	int lastID;
};
typedef struct Nodes node;
	
vector <node> Node;
vector <edge> Edge;
list <int> Queue;

int n;

int main (void) {
	int from, to, ID;
	node nod;
	edge e;
	cout << "Enter number of nodes in the graph:" << endl;
	cin >> n;
	for (int i = 0; i <= n; i++) {
		nod.inDegree = 0;
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
		e.to = to;
		e.nextID = Node[from].lastID;
		Edge.push_back(e);
		Node[from].lastID = ID;
		Node[to].inDegree += 1;
		ID += 1;
		cin >> from >> to;
	}while(from != -1);
	for (int i = 1; i <= n; i++) {
		if (Node[i].inDegree == 0) {
			Queue.push_back(i);
		}
	}
	cout << "Topological Sort gives:" << endl;
	while (!Queue.empty()) {
		from = Queue.front();
		cout << from << "\t";
		Queue.pop_front();
		for (int ID = Node[from].lastID; ID != -1; ID = Edge[ID].nextID) {
			Node[Edge[ID].to].inDegree -= 1;
			if (Node[Edge[ID].to].inDegree == 0) {
				Queue.push_back(Edge[ID].to);
			}
		}
	}
	cout << endl;
	Node.erase(Node.begin(), Node.end());
	Edge.erase(Edge.begin(), Edge.end());
	Queue.erase(Queue.begin(), Queue.end());
	return 0;
}
