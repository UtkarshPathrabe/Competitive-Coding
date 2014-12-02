/* Author: Utkarsh Pathrabe
*  Question can be found at http://www.spoj.com/problems/CRSCNTRY/
*  Algorithm: Dynamic Programming -- Longest Common Subsequence
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
	int t, i, j, temp, aglen, tolen, ma, agnes[2001], tom[2001], lcs[2][2];
	scanf("%d", &t);
	while(t--){
		temp = 1;
		aglen = 0;
		while(temp != 0){
			scanf("%d", &temp);
			agnes[aglen++] = temp;
		}
		ma = 0;
		while(1){
			scanf("%d", &temp);
			if(temp == 0){
				break;
			}else{
				tolen = 0;
				tom[tolen++] = temp;
				while(temp != 0){
					scanf("%d", &temp);
					tom[tolen++] = temp;
				}
				lcs[0][0] = lcs[0][1] = lcs[1][0] = lcs[1][1] = 0;
				for(i=0; i<aglen; i++){
					for(j=0; j<tolen; j++){
						if(agnes[i%2] == tom[j%2]){
							lcs[i%2][j%2] = 1 + lcs[(i-1)%2][(j-1)%2];
						}else{
							lcs[i%2][j%2] = max(lcs[(i-1)%2][j%2], lcs[i%2][(j-1)%2]);
						}
					}
				}
				ma = max(ma, lcs[(i-1)%2][(j-1)%2]);
			}
		}
		printf("%d\n", ma);
	}
	return 0;
}
