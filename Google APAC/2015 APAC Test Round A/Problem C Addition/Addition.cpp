#include <bits/stdc++.h>

using namespace std;

int main (void) {
	ofstream cout;
	ifstream cin;
	cout.open("C-small-practice.out");
	cin.open("C-small-practice.in");
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		map <string, map <string, int> > graph;
		map <string, map <string, int> >::iterator itmapmap;
		map <string, int>::iterator itmap;
		for (int i = 0; i < N; i++) {
			string str, a, b;
			int c;
			cin >> str;
			int ppos = str.find("+"), epos = str.find("=");
			a = str.substr(0, ppos);
			b = str.substr(ppos+1, epos-ppos-1);
			c = atoi((str.substr(epos+1)).c_str());
			itmapmap = graph.find(a);
			if (itmapmap == graph.end()) {
				map<string, int> temp;
				temp.insert(make_pair(b, c));
				graph.insert(make_pair(a, temp));
			} else {
				itmap = (itmapmap->second).find(b);
				if (itmap == (itmapmap->second).end()) {
					(itmapmap->second).insert(make_pair(b, c));
				}
			}
			itmapmap = graph.find(b);
			if (itmapmap == graph.end()) {
				map<string, int> temp;
				temp.insert(make_pair(a, c));
				graph.insert(make_pair(b, temp));
			} else {
				itmap = (itmapmap->second).find(a);
				if (itmap == (itmapmap->second).end()) {
					(itmapmap->second).insert(make_pair(a, c));
				}
			}
		}
		int V = graph.size();
		cout << "Case #" << t << ":" << endl;
		int Q;
		cin >> Q;
		for (int i = 0; i < Q; i++) {
			string str, a, b;
			cin >> str;
			int ppos = str.find("+");
			a = str.substr(0, ppos);
			b = str.substr(ppos+1);
			bool flag = false;
			int sum = 0;
			itmapmap = graph.find(a);
			if (itmapmap == graph.end()) {
				continue;
			}
			itmapmap = graph.find(b);
			if (itmapmap == graph.end()) {
				continue;
			}
			map<string, bool> visited;
			for (itmapmap = graph.begin(); itmapmap != graph.end(); itmapmap++) {
				visited[itmapmap->first] = false;
			}
			queue< pair<string, int> > q;
			for (map<string, int>::iterator it1 = graph[b].begin(); it1 != graph[b].end(); it1++) {
				visited[it1->first] = true;
				q.push(make_pair(it1->first, it1->second));
			}
			while (!q.empty()) {
				pair<string, int> now = q.front();
				q.pop();
				if ((now.first).compare(a) == 0) {
					cout << a << "+" << b << "=" << now.second << endl;
					break;
				}
				for (map<string, int>::iterator it1 = graph[now.first].begin(); it1 != graph[now.first].end(); it1++) {
					for (map<string, int>::iterator it2 = graph[it1->first].begin(); it2 != graph[it1->first].end(); it2++) {
						if (visited[it2->first] == false) {
							visited[it2->first] = true;
							q.push(make_pair(it2->first, now.second - it1->second + it2->second));
						}
					}
				}
			}
		}
	}
	cout.close();
	cin.close();
	return 0;
}
