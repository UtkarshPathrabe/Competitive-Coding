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

void mirror(struct node* root) {
    if(root == NULL){
         return;
    }
    mirror(root->left);
    mirror(root->right);
    struct node* temp = root->left;
    root->left = root->right;
    root->right = temp;
}

int isSameStruct(struct node* n1, struct node* n2){
    if (n1 == NULL && n2 == NULL) {
          return 1;
    }
    if (n1 != NULL && n2 != NULL && isSameStruct(n1->left, n2->left) && isSameStruct(n1->right, n2->right)) {
          return 1;
    }
    return 0;
}

int isFoldable(struct node* root){
    if(root == NULL) {
            return 1;
    }
    mirror(root->left);
    int ans = isSameStruct(root->left, root->right);
    mirror(root->left);
    return ans;
}

int main (void) {
    struct node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->right = newNode(4);
    root->right->left = newNode(5);
    if (isFoldable(root)) {
          cout << "Tree is foldable." << endl;
    }else{
          cout << "Tree is not foldable." << endl;
    } 
    return 0;
}
