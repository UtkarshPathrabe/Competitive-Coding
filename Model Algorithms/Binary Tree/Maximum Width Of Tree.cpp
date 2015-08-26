#include <bits/stdc++.h>

using namespace std;

struct node{
       int data;
       struct node* left;
       struct node* right;
};

struct node* newNode(int data) {
       struct node* temp = (struct node*)malloc(sizeof(struct node));
       temp->data = data;
       temp->left = NULL;
       temp->right = NULL;
       return temp;
}

int height (struct node* temp) {
    if (temp == NULL) {
          return 0;
    }
    return (1 + ((height(temp->left) > height(temp->right))? height(temp->left) : height(temp->right)));
}

int getMax(int *width, int l) {
    int m = width[0];
    for (int i = 1; i < l; i++) {
        m = ((m > width[i])? m : width[i]);
    }
    return m;
}

void getMaxWidthRecur(struct node* root, int *width, int level) {
     if (root == NULL) {
           return;
     }
     width[level]++;
     getMaxWidthRecur(root->left, width, level+1);
     getMaxWidthRecur(root->right, width, level+1);
}

int getMaxWidth(struct node* root) {
    int h = height(root);
    int *width = (int *)calloc(sizeof(int), h);
    getMaxWidthRecur(root, width, 0);
    return getMax(width, h);
}

int main (void) {
    struct node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->right = newNode(8);
    root->right->right->left = newNode(6);
    root->right->right->right = newNode(7);
    cout << "Maximum width of tree is " << getMaxWidth(root) << endl;
    return 0;
}
