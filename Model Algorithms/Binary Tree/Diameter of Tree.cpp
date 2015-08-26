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

int max (int a, int b) {
	return (a > b) ? a : b;
}

int height (struct node* temp) {
	if (temp == NULL) {
		return 0;
	} else {
		return 1 + max(height(temp->left), height(temp->right));
	}
}

int diameter (struct node* temp) {
	if (temp == NULL) {
		return 0;
	}
	int lh = height(temp->left), rh = height(temp->right), ld = diameter(temp->left), rd = diameter(temp->right);
	return max(max(ld, rd), (1 + rh + lh));
}

int diameterOpt (struct node* temp, int *h) {
	int lh = 0, rh = 0, ld = 0, rd = 0;
	if (temp == NULL) {
		*h = 0;
		return 0;
	}
	ld = diameterOpt(temp->left, &lh);
	rd = diameterOpt(temp->right, &rh);
	*h = max(lh, rh) + 1;
	return max(max(ld, rd), lh + rh + 1);
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	root->right->right = newNode(7);
	int h = 0;
	printf("The diameter of the tree is %d.\n", diameter(root));
	printf("The diameter of the tree is %d.\n", diameterOpt(root, &h));
	return 0;
}
