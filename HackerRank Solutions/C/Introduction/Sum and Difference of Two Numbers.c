#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a, b;
    scanf("%d %d", &a, &b);
    printf("%d %d\n", a + b, a - b);
    float c, d;
    scanf("%f %f", &c, &d);
    printf("%.1f %.1f", c + d, c - d);
    return 0;
}