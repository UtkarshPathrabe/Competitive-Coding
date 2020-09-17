#include <stdio.h>

void update(int *a, int *b) {
    // Complete this function  
    int sum = *a + *b;
    int difference;
    if (*a >= *b) {
        difference = *a - *b;
    } else {
        difference = *b - *a;
    }
    *a = sum;
    *b = difference;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}