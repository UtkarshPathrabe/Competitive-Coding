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

int max(int a, int b) {
	return (a > b) ? a : b;
}

int height (struct node* temp) {
	if (temp == NULL) {
		return 0;
	}
	return (1 + max(height(temp->left), height(temp->right)));
}

int abs (int n) {
	if (n < 0) {
		return (-n);
	} else {
		return n;
	}
}

int isBalanced (struct node* temp) {
	if (temp == NULL) {
		return 1;
	}
	int lh = height(temp->left), rh = height(temp->right);
	if ((abs(lh - rh) <= 1) && isBalanced(temp->left) && isBalanced(temp->right)) {
		return 1;
	}
	return 0;
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	root->right->right = newNode(7);
	if (isBalanced(root)) {
		printf ("The tree is balanced.\n");
	} else {
		printf ("The tree is not balanced.\n");
	}
	return 0;
}
