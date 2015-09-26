#include<stdio.h>

int main()
{
    int arr[505]={0},i,j,n,s;

    scanf("%i%i",&n,&s);

    if(s < 0)
    {
        j = (n*(n+1))/2;

        if( (j+s)&1 || j <= -1*s )
        {
            printf("Impossible\n");
        }

        else
        {
            j = (j + s)/2 - 1;

            i = n+1;
            while(--i > 1 && j)
            {
                if( j - i > 1)
                {
                    j -= i;
                    arr[i] = 1;
                }

                else if(j-i == 0)
                {
                    j -= i;
                    arr[i] = 1;
                    break;
                }
            }

            if(j)
                printf("Impossible\n");
            else
            {
                printf("1");

                i = 1;
                while(++i <= n)
                {
                    arr[i] ? printf("+%i",i) : printf("-%i",i);
                }

                printf("\n");
            }

        }
    }

    else
    {
        j = (n*(n+1))/2;

        if( (j-s)&1 || j < s )
        {
            printf("Impossible\n");
        }

        else
        {
            j = (j - s)/2;

            i = n+1;
            while(--i > 1 && j)
            {
                if( j - i > 1)
                {
                    j -= i;
                    arr[i] = 1;
                }

                else if(j-i == 0)
                {
                    j -= i;
                    arr[i] = 1;
                    break;
                }
            }

            if(j)
            {
                printf("Impossible\n");
            }

            else
            {
                printf("1");

                i = 1;
                while(++i <= n)
                {
                    arr[i] ? printf("-%i",i) : printf("+%i",i);
                }

                printf("\n");
            }
        }
    }

    return 0;
}
