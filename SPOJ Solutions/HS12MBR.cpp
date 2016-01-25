#include <bits/stdc++.h>

using namespace std;

int main (void) {
	int t;
	cin >> t;
	while (t--) {
		int n, xmin = 1000, ymin = 1000, xmax = -1000, ymax = -1000;
		cin >> n;
		for (int i = 0; i < n; i++) {
			char type;
			cin >> type;
			if (type == 'p') {
				int x, y;
				cin >> x >> y;
				xmin = min (xmin, x);
				ymin = min (ymin, y);
				xmax = max (xmax, x);
				ymax = max (ymax, y);
			} else if (type == 'c') {
				int x, y, r;
				cin >> x >> y >> r;
				xmin = min (xmin, x-r);
				ymin = min (ymin, y-r);
				xmax = max (xmax, x+r);
				ymax = max (ymax, y+r);
			} else if (type == 'l') {
				int x1, x2, y1, y2;
				cin >> x1 >> y1 >> x2 >> y2;
				xmin = min (xmin, min (x1, x2));
				ymin = min (ymin, min (y1, y2));
				xmax = max (xmax, max (x1, x2));
				ymax = max (ymax, max (y1, y2));
			}
		}
		cout << xmin << " " << ymin << " " << xmax << " " << ymax << endl; 
	}
	return 0;
}
