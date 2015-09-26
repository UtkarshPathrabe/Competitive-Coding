#include <iostream>
#include <cstdio>
#include <cmath>
 
using namespace std;
 
int main () {
    unsigned long long t, x, y, s, a, r, n, i, p, term;
    scanf("%lld", &t);
    while (t--) {
        scanf("%lld %lld %lld", &x, &y, &s);
        i = 0;
        if (x == y) {
            r = 1;
            n = (unsigned long long)(s/x);
            printf("%lld\n", n);
            while (i < n-1) {
                printf("%lld ", x);
                i++;
            }
            printf("%lld\n", x);
        }else {
            if (s == 0) {
                s--;
            }
            p = (unsigned long long)(s/y);
            r = (unsigned long long)((-1+sqrt(1-4*(1-p)))/2.0);
            a = x/(r*r);
            n = (unsigned long long)(log (y/a)/log (r))+3;
            if (a*pow (r, n-2) == y) {
                n++;
            }
            printf("%lld\n", n);
            term = 1;
            while (i < n-1) {
                printf("%lld ", a*term);
                term = term*r;
                i++;
            }
            printf("%lld\n", a*term);
        }
    }
    return 0;
}
