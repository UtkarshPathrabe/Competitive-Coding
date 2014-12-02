/* Author: Utkarsh Pathrabe
*  Question can be found at http://www.spoj.com/problems/FCTRL2/
*  Algorithms: Dynamic Programming
*/

#include <stdio.h>

int main() {
    int cases, num, i, k, j, carry;
    scanf("%d", &cases);
    while(cases--) {
		k = 0;
		carry = 0;
		int  arr[1000] = {1};
        scanf("%d", &num);
        for(i = 1; i <= num; i++) {
            for(j = 0; j <= k; j++) {
                arr[j] = arr[j] * i + carry;
                carry = arr[j] / 10;
                arr[j] = arr[j] % 10;
             }
             while(carry) {
                k++;
                arr[k] = carry % 10;
                carry /= 10;
             }
         }
         for(i = k; i >= 0; i--)
            printf("%d", arr[i]);
        printf("\n");
    }
    return 0;
}