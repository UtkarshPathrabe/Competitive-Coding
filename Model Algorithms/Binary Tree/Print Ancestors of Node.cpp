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

int printAncestors(struct node* temp, int data) {
	if (temp == NULL) {
		return 0;
	}
	if (temp->data == data) {
		return 1;
	}
	if ((printAncestors(temp->left, data)) || (printAncestors(temp->right, data))) {
		printf("%d\t", temp->data);
		return 1;
	} else {
		return 0;
	}
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	root->right->right = newNode(7);
	root->left->left->left = newNode(8);
	printAncestors(root, 8);
	return 0;
}
