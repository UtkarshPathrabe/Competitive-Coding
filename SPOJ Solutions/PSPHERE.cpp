#include <cmath>
#include <cstdio>
#include <iomanip>
#include <iostream>

using namespace std;
 
int main(){
	int nTestCases = 0;
	scanf("%d", &nTestCases);
	for(int i =0; i<nTestCases; i++){
		int n = 0;
		scanf("%d", &n);
		double s = sqrt(n * 1.0)/3.6;
		double dz = 2.0/n;
		double l = 0;
		double z = 1.0 - dz/2.0;
		for(int k = 0; k <= n-1; k++){
			double r = sqrt(1 - z *z);
			cout << setiosflags(ios::fixed) << setprecision(6) << cos(l) * r << " " << sin(l) * r << " " << z << "\n";
			z = z -dz;
			l = l + s/r;
		}
	}
	return 0;
}
