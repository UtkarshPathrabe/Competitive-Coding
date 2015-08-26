#include <bits/stdc++.h>

using namespace std;

struct node{
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

int ceil (struct node* root, int data) {
	if (root == NULL) {
		return -1;
	}
	if (root->data == data) {
		return data;
	}
	if (root->data < data) {
		return ceil(root->right, data);
	}
	int c = ceil(root->left, data);
	return (c >= data) ? c : root->data;
}

int main (void) {
	struct node* root = newNode(8);
	root->left = newNode(4);
	root->right = newNode(12);
	root->left->left = newNode(2);
	root->left->right = newNode(6);
	root->right->left = newNode(10);
	root->right->right = newNode(14);
	for (int i = 0; i < 16; i++) {
		printf("%d\t:%d\n", i, ceil(root, i));
	}
	return 0;
}
