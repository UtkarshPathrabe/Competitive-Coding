/* Author: Utkarsh Pathrabe
*  Question can be found at: http://www.spoj.com/problems/CISTFILL/
*  Algorithms: Binary Search
*/

#include <bits/stdc++.h>

using namespace std;

struct Cistern{
	int base;
	int height;
	int width;
	int depth;
};

int main(void) {
	int k, n;
	double V, volume, highLevel, lowLevel, presentLevel;
	struct Cistern cis;
	vector<Cistern> Cisterns;
	vector<Cistern>::iterator it;
	scanf("%d", &k);
	while(k--) {
		volume = 0.0;
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			scanf("%d %d %d %d", &cis.base, &cis.height, &cis.width, &cis.depth);
			volume += (cis.height * cis.width * cis.depth);
			Cisterns.push_back(cis);
		}
		scanf("%lf", &V);
		if(volume < V) {
			printf("OVERFLOW\n");
		}else{
			lowLevel = 0.0;
			highLevel = 1e7;
			while(highLevel - lowLevel > 0.000001) {
				presentLevel = (highLevel + lowLevel) / 2;
				volume = 0.0;
				for(it = Cisterns.begin(); it != Cisterns.end(); it++) {
					if((*it).base >= presentLevel){
						continue;
					}else if(((*it).base < presentLevel) && (((*it).base + (*it).height) >= presentLevel)) {
						volume += ((presentLevel - (*it).base) * ((*it).width) * ((*it).depth));
					}else if(((*it).base + (*it).height) < presentLevel) {
						volume += (((*it).height) * ((*it).width) * ((*it).depth));
					}
				}
				if(volume >= V) {
					highLevel = presentLevel;
				}else{
					lowLevel = presentLevel;
				}
			}
			printf("%.2lf\n", presentLevel);
		}
		Cisterns.erase(Cisterns.begin(), Cisterns.end());
	}
	return 0;
}
