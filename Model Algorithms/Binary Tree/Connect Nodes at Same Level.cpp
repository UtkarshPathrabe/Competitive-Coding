#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node* left;
	struct node* right;
	struct node* nextRight;
};

struct node* newNode (int num) {
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	temp->nextRight = NULL;
	return temp;
}

void connectRecur(struct node* temp) {
	if (temp == NULL) {
		return;
	}
	if (temp->left) {
		temp->left->nextRight = temp->right;
	}
	if (temp->right) {
		temp->right->nextRight = ((temp->nextRight)?(temp->nextRight->left):NULL);
	}
	connectRecur(temp->left);
	connectRecur(temp->right);
}

void connect(struct node* temp) {
	temp->nextRight = NULL;
	connectRecur(temp);
}

int main (void) {
	struct node* root = newNode(10);
	root->left = newNode(8);
	root->right = newNode(2);
	root->left->left = newNode(3);
	connect(root);
	printf ("Following are populated nextRight pointers in the tree (-1 is printed if there is no nextRight)");
	printf ("\nnextRight of %d is %d", root->data, root->nextRight ? root->nextRight->data:-1);
	printf ("\nnextRight of %d is %d", root->left->data, root->left->nextRight ? root->left->nextRight->data:-1);
	printf ("\nnextRight of %d is %d", root->right->data, root->right->nextRight ? root->right->nextRight->data:-1);
	printf ("\nnextRight of %d is %d", root->left->left->data, root->left->left->nextRight ? root->left->left->nextRight->data:-1);
	return 0;
}
