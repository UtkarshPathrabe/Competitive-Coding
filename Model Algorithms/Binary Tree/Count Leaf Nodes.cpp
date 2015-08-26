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

int countLeafNode (struct node* temp) {
	if (temp == NULL) {
		return 0;
	} else if (temp->left == NULL && temp->right == NULL) {
		return 1;
	} else {
		return (countLeafNode(temp->left) + countLeafNode(temp->right));
	}
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	printf ("The number of leaf nodes are %d.\n", countLeafNode(root));
	return 0;
}
