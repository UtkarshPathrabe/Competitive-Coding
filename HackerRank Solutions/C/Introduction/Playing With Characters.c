#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    char ch;
    scanf("%c", &ch);
    printf("%c\n", ch);
    scanf("%c", &ch);
    char s[100];
    scanf("%s", s);
    printf("%s\n", s);
    scanf("%c", &ch);
    char sentence[100];
    scanf("%[^\n]%*c", sentence);
    printf("%s\n", sentence);   
    return 0;
}