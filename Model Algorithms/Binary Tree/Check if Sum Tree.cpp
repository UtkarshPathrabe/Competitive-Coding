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

int isLeaf(struct node* temp) {
	if (temp == NULL) {
		return 0;
	}
	if ((temp->left == NULL) && (temp->right == NULL)) {
		return 1;
	}
	return 0;
}

int isSumTree (struct node* temp) {
	int lsum = 0, rsum = 0;
	if ((temp == NULL) || (isLeaf(temp))) {
		return 1;
	}
	if (isSumTree(temp->left) && isSumTree(temp->right)) {
		if (temp->left == NULL) {
			lsum = 0;
		} else if (isLeaf(temp->left)) {
			lsum = temp->left->data;
		} else {
			lsum = (2 * temp->left->data);
		}
		if (temp->right == NULL) {
			rsum = 0;
		} else if (isLeaf(temp->right)) {
			rsum = temp->right->data;
		} else {
			rsum = (2 * temp->right->data);
		}
		return (temp->data == lsum + rsum);
	}
	return 0;
}

int main (void) {
	struct node* root = newNode(26);
	root->left = newNode(10);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(6);
	root->right->right = newNode(3);
	if (isSumTree(root)) {
		printf("The given tree is a Sum Tree.\n");
	} else {
		printf("The given tree is not a Sum Tree.\n");
	}
	return 0;
}
