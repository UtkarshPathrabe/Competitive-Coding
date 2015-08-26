#include <bits/stdc++.h>

using namespace std;

struct node{
       int data;
       struct node* left;
       struct node* right;
};

struct node* newNode(int num) {
       struct node* temp = (struct node*)malloc(sizeof(struct node));
       temp->data = num;
       temp->left = NULL;
       temp->right = NULL;
       return temp;
}

void morrisTraversal (struct node* root) {
     if (root == NULL) {
           return;
     }
     struct node *curr = root, *pre;
     while(curr != NULL){
             if (curr->left == NULL) {
                   printf("%d\t", curr->data);
                   curr = curr->right;
             } else {
                    pre = curr->left;
                    while (pre->right != NULL && pre->right != curr) {
                          pre = pre->right;
                    }
                    if (pre->right == NULL) {
                          pre->right = curr;
                          curr = curr->left;
                    } else {
                           pre->right = NULL;
                           printf("%d\t", curr->data);
                           curr = curr->right;
                    }
             }
     }
}

int main(void) {
    struct node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    morrisTraversal(root);
    return 0;
}
