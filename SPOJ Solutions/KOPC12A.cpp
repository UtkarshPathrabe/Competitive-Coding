/* Author: Utkarsh Pathrabe
*  Question can be found at: http://www.spoj.com/problems/KOPC12A/
*  Algorithms: Binary Search
*/

#include <bits/stdc++.h>

using namespace std;

struct Building{
	short height;
	short cost;
};
vector<Building> Buildings;
vector<Building>::iterator it;

long long int ComputeCost(const Building &P) {
	long long int result = 0;
	for(it = Buildings.begin(); it != Buildings.end(); it++) {
		result += abs((*it).height - P.height) * (*it).cost;
	}
	return result;
}

bool compare(const Building &P, const Building &Q) {
	return ComputeCost(P) < ComputeCost(Q);
}

int main(void) {
	short test, N;
	struct Building build;
	scanf("%hd", &test);
	while(test--) {
		scanf("%hd", &N);
		for(int i = 0; i < N; i++) {
			scanf("%hd", &build.height);
			Buildings.push_back(build);
		}
		for(it = Buildings.begin(); it != Buildings.end(); it++) {
			scanf("%hd", &(*it).cost);
		}
		sort(Buildings.begin(), Buildings.end(), compare);
		printf("%lld\n", ComputeCost(Buildings[0]));
		Buildings.erase(Buildings.begin(), Buildings.end());
	}
	return 0;
}
