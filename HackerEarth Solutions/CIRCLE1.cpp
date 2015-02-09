#include<bits/stdc++.h>

using namespace std ;

typedef complex<double> point ;

struct circle {
    point c ; double r ;
    circle (point c, double r):c(c), r(r) {}
    circle() {}
};

double calculate_area (circle & a, circle &b) {
    double d = abs (b.c - a.c );
    //cout << " d: " << d << " " << "circle1 : " << real(a.c) << " " << imag(a.c) << " , radius : " << b.r << " , " << a.r << endl ;
    if (d <= (b.r - a.r)) 
		return a.r*a.r*M_PI;
    if (d <= (a.r - b.r)) 
		return b.r*b.r*M_PI;
    if (d >= a.r + b.r) 
		return 0;
    double alpha = acos ((a.r*a.r + d*d - b.r*b.r) / (2*a.r*d));
    double beta = acos ((b.r*b.r + d*d - a.r*a.r) / (2*b.r*d));
    return a.r*a.r*(alpha-0.5*sin(2*alpha)) + b.r*b.r*(beta-0.5*sin(2*beta));
}

int main() {
    //freopen("in.txt","r",stdin) ;
    //freopen("out.txt","w",stdout) ;
    int t, n, x1, y2, y1, x2, x;
    cin >> t ;
    while (t--) {
        cin >> n >> x1 >> y1 >> x2 >> y2;
        int r1 = 10000000, r2 = 10000000;
        for (int i = 0; i < n; i++) {
			cin >> x; 
			r1 = min(r1,x); 
		}
        for (int i = 0; i < n; i++) {
			cin >> x; 
			r2 = min(r2,x);
		}
        complex<double> p1 (x1, y1), p2 (x2, y2);
        circle c1 (p1, r1), c2 (p2, r2);
        double ans = calculate_area (c1, c2);
        printf ("%.2lf\n", ans);
    }
    return 0 ;
}
