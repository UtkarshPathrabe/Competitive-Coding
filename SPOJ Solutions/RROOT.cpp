#include<cstdio>
#include<cmath>

int main(){
    int t;
	double d;
    scanf("%i", &t);
    while(t--){
		scanf("%lf", &d);
		printf("%0.6lf\n", 1 - 1/(3*sqrt(d/2)));
    }
    return 0;
}