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

struct node* insert (struct node* root, int data) {
	if (root == NULL) {
		return newNode(data);
	}
	if (data <= root->data) {
		root->left = insert(root->left, data);
	} else {
		root->right = insert(root->right, data);
	}
	return root;
}

void inOrder (struct node* root) {
	if (root != NULL) {
		inOrder(root->left);
		printf ("%d\t", root->data);
		inOrder(root->right);
	}
}

struct node* removeOutsideRange (struct node* root, int min, int max) {
	if (root == NULL) {
		return NULL;
	}
	root->left = removeOutsideRange(root->left, min, max);
	root->right = removeOutsideRange(root->right, min, max);
	if (root->data < min) {
		struct node* rChild = root->right;
		free(root);
		return rChild;
	} else if (root->data > max) {
		struct node* lChild = root->left;
		free(root);
		return lChild;
	}
	return root;
}

int main (void) {
	struct node* root = NULL;
	root = insert(root, 6);
	root = insert(root, -13);
	root = insert(root, 14);
	root = insert(root, -8);
	root = insert(root, 15);
	root = insert(root, 13);
	root = insert(root, 7);
	printf("In Order Traversal of given tree:\n");
	inOrder(root);
	root = removeOutsideRange(root, -10, 13);
	printf("\nIn Order Traversal of modified tree:\n");
	inOrder(root);
	return 0;
}
