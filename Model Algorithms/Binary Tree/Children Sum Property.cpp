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

int checkSum(struct node* temp) {
	if ((temp == NULL) || (temp->left == NULL && temp->right == NULL)) {
		return 1;
	} else {
		int l = 0, r = 0;
		if (temp->left) {
			l = temp->left->data;
		}
		if (temp->right) {
			r = temp->right->data;
		}
		if ((temp->data == (l + r)) && checkSum(temp->left) && checkSum(temp->right)) {
			return 1;
		} else {
			return 0;
		}
	}
}

int main (void) {
	struct node* root = newNode(10);
	root->left = newNode(8);
	root->right = newNode(2);
	root->left->left = newNode(3);
	root->left->right = newNode(5);
	root->right->right = newNode(2);
	if (checkSum(root)) {
		printf("The given tree satisfies the children sum property.\n");
	} else {
		printf("The given tree does not satisfy the children sum property.\n");
	}
	return 0;
}
