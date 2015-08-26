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

int sumTree(struct node* temp) {
    if (temp == NULL) {
          return 0;
    }
    int old = temp->data;
    temp->data = sumTree(temp->left) + sumTree(temp->right);
    return (temp->data + old); 
}

void printInorder(struct node* temp) {
     if (temp == NULL) {
           return;
     }
     printInorder(temp->left);
     printf("%d\t", temp->data);
     printInorder(temp->right);
}

int main (void) {
    struct node* root = newNode(10);\
    root->left = newNode(-2);
    root->right = newNode(6);
    root->left->left = newNode(8);
    root->left->right = newNode(-4);
    root->right->left = newNode(7);
    root->right->right = newNode(5);
    sumTree(root);
    printInorder(root);
    return 0;
}
