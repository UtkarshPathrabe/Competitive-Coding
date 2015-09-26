#include <bits/stdc++.h> 
using namespace std;
#define MOD 1000000007
int main() { 
    int t;
    scanf("%d ",&t); 
    for(int p=1;p<=t;p++) { 
        char s[10009]; 
        scanf("%s", s);
        int prev[11];
        for(int i=0; i<10; i++) 
            prev[i] = 0; 
        int sum = 0; 
        int j=-1, k, temp;
        while(s[++j] != '\0') {
            k = s[j] - 48; 
            temp = k; 
            while(k--)
                prev[temp] = (prev[temp]+ prev[k])%MOD;
            prev[temp]++;
        }
        for(int i=0;i<=9;i++)
            sum = (sum + prev[i])%MOD;
        printf("Case %d: %d\n",p,sum);
    }
    return 0; 
}
