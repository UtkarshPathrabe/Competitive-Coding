#include<stdio.h>
#include<stdlib.h>

struct node
{
    int val;
    struct node *left,*right;

}*start=NULL,*med=NULL,*temp;

int main()
{
    int n,count=0;

    while(scanf("%i",&n)!=EOF)
    {
        if(n>0)
        {
            ++count;

            temp = (struct node *)malloc(sizeof(temp));

            temp->val = n;
            temp->left = temp->right = NULL;

            if(med==NULL)
            {
                start = med = temp;
            }

            else
            {
                start->right = temp;
                temp->left = start;
                start = temp;

                if(count&1)
                {
                    med = med->right;
                }
            }
        }

        else if(n==-1)
        {
            temp = med;

            printf("%d\n",med->val);

            if(count&1)
                med = med->left;
            else
                med = med->right;

            count--;

            if(temp->left != NULL)
                temp->left->right = temp->right;
            if(temp->right != NULL)
                temp->right->left = temp->left;

            free(temp);
        }

        else
        {
            printf("\n");
            start = med = NULL;
            count = 0;
            fflush(stdin);
        }
    }

    return 0;
}
