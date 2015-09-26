#include<stdio.h>

int main()
{
  int i,j,k,index,org_index,str_len,key_len,count; char str[500],key[20],result[255][255][2];

    while( scanf("%s%s",key,str) != EOF )
    {
        str_len = key_len = -1;
        while(str[++str_len] != 0);
        while(key[++key_len] != 0);

        i = -1;
        k = str_len / key_len;
        while(++i <=  k+1 )
        {
            j = -1;
            while(++j <= key_len)
                result[i][j][0] = result[i][j][1] = 0;
        }

        count = 0;
        k = str_len;
        i = org_index = -1;
        while( ++i < 255 && k)
        {
            j = -1;
            while(++j < key_len && k)
            {
                ++count;
                result[i][j][0] = str[++org_index];
                k--;

                if(count&1 && k)
                {
                    result[i][j][1] = str[++org_index];
                    k--;
                }
            }
        }

        k = key_len;
        while(k--)
        {
            char ch = 'a';

            i = -1;
            while(key[++i] != 0)
                if(key[i] < ch)
                {
                    index = i;
                    ch = key[i];
                }

            i=-1;
            while(++i<255)
            {
                if( result[i][index][0] == 0 && result[i][index][1] == 0 )
                    break;

                printf("%c",result[i][index][0]);

                if(result[i][index][1])
                    printf("%c",result[i][index][1]);
            }

            key[index] = 'a';
        }

        printf("\n");

    }

    return 0;
}
