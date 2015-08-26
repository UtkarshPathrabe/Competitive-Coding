#include <bits/stdc++.h>

using namespace std;

struct node {
       int data;
       struct node* left;
       struct node* right;
       struct node* next;
};

struct node* newNode(int num) {
       struct node* temp = (struct node*)malloc(sizeof(struct node));
       temp->data = num;
       temp->left = NULL;
       temp->right = NULL;
       temp->next = NULL;
       return temp;
}

void populateNext (struct node* temp) {
     static struct node* next = NULL;
     if (temp) {
           populateNext(temp->right);
           temp->next = next;
           next = temp;
           populateNext(temp->left);
     }
}

int main (void) {
    struct node* root = newNode(10);
    root->left = newNode(8);
    root->right = newNode(12);
    root->left->left = newNode(3);
    populateNext(root);
    struct node* ptr = root->left->left;
    while(ptr){
            printf("Next of %d is %d\n", ptr->data, ptr->next ? ptr->next->data:-1);
            ptr = ptr->next;
    }
    return 0;
}
