#include <bits/stdc++.h>

using namespace std;

vector<int> seq[1000001];
int indegree[1000001] = {0};
bool valid[1000001] = {false};
priority_queue<int, vector<int>, greater<int> > pqueue;

int main (void) {
	int N, K, maxVal = INT_MIN, temp, prev;
	cin >> N;
	while (N--) {
		cin >> K;
		for (int i = 0; i < K; i++) {
			cin >> temp;
			valid[temp] = true;
			maxVal = max (maxVal, temp);
			if (i) {
				seq[prev].push_back (temp);
				indegree[temp]++;
			}
			prev = temp;
		}
	}
	for (int i = 1; i <= maxVal; i++) {
		if ((indegree[i] == 0) && (valid[i])) {
			pqueue.push(i);
		}
	}
	while (!pqueue.empty()) {
		temp = pqueue.top();
		cout << temp << " ";
		pqueue.pop();
		for (int i = 0; i < seq[temp].size(); i++) {
			prev = seq[temp][i];
			if (((--indegree[prev]) == 0) && (valid[prev])) {
				pqueue.push(prev);
			}
		}
	}
	cout << endl;
	return 0;
}
