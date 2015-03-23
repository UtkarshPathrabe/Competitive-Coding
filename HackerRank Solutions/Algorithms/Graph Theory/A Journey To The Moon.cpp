#include <bits/stdc++.h>

using namespace std;

class UnionFind {
	private:
		vector<int> p;
	vector<int> rank;
	public:
		UnionFind (int N) {
	    	p.assign(N, 0);
	    	rank.assign(N, 0);
	    	for (int i = 0; i < N; i++)
			    p[i] = i;
		}
		int findSet (int i) {
		    return (p[i] == i ? i : (p[i] = findSet (p[i])));
		}
		bool isSameSet (int i, int j) {
		    return findSet (i) == findSet (j);
		}
		void unionSet (int i, int j) {
			if (!isSameSet(i, j)) {
			    int x = findSet(i);
			    int y = findSet(j);
				if (rank[x] > rank[y])
			    	p[y] = x;
				else {
					p[x] = y;
					if (rank[x] == rank[y])
						rank[y]++;
				}
			}
		}
};

long long getNumberOfWaysToPair (int N, vector<pair<int, int> > sameCountry) {
	int I = sameCountry.size();
	UnionFind uf (N);
	for (int i = 0; i < I; i++) {
		uf.unionSet(sameCountry[i].first, sameCountry[i].second);
	}
	map<int, int> countryCount;
	for (int i = 0; i < N; i++) {
		countryCount[uf.findSet(i)]++;
	}
	long long total = 0;
	for (int i = 0; i < N; i++) {
		total += N - countryCount[uf.findSet(i)];
	}
	return total / 2;
}

int main (void) {
	int N, I;
	vector<pair<int, int> > sameCountry;
	cin >> N >> I;
	for (int i = 0; i < I; i++) {
		pair<int, int> p;
		cin >> p.first >> p.second;
		sameCountry.push_back (p);
	}
	cout << getNumberOfWaysToPair (N, sameCountry) << endl;
	return 0;
}
