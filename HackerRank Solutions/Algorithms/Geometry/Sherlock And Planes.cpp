#include <bits/stdc++.h>

using namespace std;

typedef struct Point {
	int x;
	int y;
	int z;
} Point;

int main (void) {
	int T, x, y, z;
	cin >> T;
	while (T--) {
		cin >> x >> y >> z;
		Point a = {x, y, z};
		cin >> x >> y >> z;
		Point b = {x, y, z};
		cin >> x >> y >> z;
		Point c = {x, y, z};
		cin >> x >> y >> z;
		Point d = {x, y, z};
		Point ab = {(b.x - a.x), (b.y - a.y), (b.z - a.z)};
		Point ac = {(c.x - a.x), (c.y - a.y), (c.z - a.z)};
		Point ad = {(d.x - a.x), (d.y - a.y), (d.z - a.z)};
		int det1 = (ac.y * ad.z) - (ad.y * ac.z);
		int det2 = (ab.y * ad.z) - (ad.y * ab.z);
		int det3 = (ab.y * ac.z) - (ac.y * ab.z);
		int detTotal = (ab.x * det1) - (ac.x * det2) + (ad.x * det3);
		if(detTotal == 0){
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
	return 0;
}
