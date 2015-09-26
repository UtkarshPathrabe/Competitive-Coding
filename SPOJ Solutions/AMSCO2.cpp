#include<stdio.h>

int main()
{
    int i,j,k,len_str,len_key,index,enc_index;  char ch,key[100],str[300];

    while(scanf("%s%s",key,str) != EOF)
    {
        int count = 0;    char hold[255][255] = {0},result[255][255][2];

        len_str = -1;
        while(str[++len_str] != 0);
        len_key = -1;
        while(key[++len_key] != 0);

        i = -1;
        k = len_str/len_key + 1;
        while(++i <= k)
        {
            j = -1;
            while(++j <= len_key)
                result[i][j][0] = result[i][j][1] = 0;
        }

        i=-1;
        k = len_str;
        while(++i < 255 && k)
        {
            j=-1;
            while(++j < len_key && k)
            {
                ++count;

                if(count&1 && k >= 2)
                {
                    hold[i][j] = '2';
                    k -= 2;
                }
                else
                {
                    hold[i][j] = '1';
                    k--;
                }
            }
        }

        enc_index = -1;
        k = len_key;
        while(k--)
        {
            ch = 'a';

            i = -1;
            while(key[++i]!=0)
                if(ch > key[i])
                {
                    index = i;
                    ch = key[i];
                }

            i = -1;
            while(hold[++i][index])
            {
                result[i][index][0] = str[++enc_index];

                if(hold[i][index] == '2')
                {
                    result[i][index][1] = str[++enc_index];
                }
            }

            key[index] = 'a';
        }

        i = -1;
        k = len_str;

        while(++i <255 && k)
        {
            j = -1;
            while(++j < len_key && k)
            {
                printf("%c",result[i][j][0]);
                k--;
                if(result[i][j][1])
                {
                    printf("%c",result[i][j][1]);
                    k--;
                }
            }
        }

        printf("\n");
    }

    return 0;
}
