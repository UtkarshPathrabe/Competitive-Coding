#include <bits/stdc++.h>

using namespace std;

struct node {
    int data;
    struct node* left;
    struct node* right;
};

struct node* newNode (int num) {
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = num;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

int hasPathSum (struct node* temp, int sum) {
    if (temp == NULL) {
          return (sum == 0);
    } else {
           int ans = 0, subSum = sum - temp->data;
           if (subSum == 0 && temp->left == NULL && temp->right == NULL) {
                 return 1;
           }
           if (temp->left) {
                 ans = ans || hasPathSum(temp->left, subSum);
           }
           if (temp->right) {
                 ans = ans || hasPathSum(temp->right, subSum);
           }
           return ans;
    }
}

int main (void) {
    struct node* root = newNode(10);
    root->left = newNode(8);
    root->right = newNode(2);
    root->left->left = newNode(3);
    root->left->right = newNode(5);
    root->right->left = newNode(2);
    int sum = 21;
    if (hasPathSum(root, sum)) {
       printf("Tree has a path with sum %d.\n", sum);
    } else {
       printf("Tree doesn't have a path with sum %d.\n", sum);
    }
    return 0;
}
