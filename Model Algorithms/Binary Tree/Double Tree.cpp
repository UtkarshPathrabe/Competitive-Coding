#include <bits/stdc++.h>

using namespace std;

struct node {
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

void doubleTree(struct node* temp) {
     if (temp == NULL) {
           return;
     }
     doubleTree(temp->left);
     doubleTree(temp->right);
     struct node* old = temp->left;
     temp->left = newNode(temp->data);
     temp->left->left = old;
}

void printInOrder (struct node* temp) {
     if (temp == NULL) {
           return;
     }
     printInOrder(temp->left);
     printf("%d\t", temp->data);
     printInOrder(temp->right);
}

int main (void) {
    struct node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    printf("In Order traversal of original tree is:\n");
    printInOrder(root);
    doubleTree(root);
    printf("\nIn Order traversal of double tree is:\n");
    printInOrder(root);
    return 0;
}
