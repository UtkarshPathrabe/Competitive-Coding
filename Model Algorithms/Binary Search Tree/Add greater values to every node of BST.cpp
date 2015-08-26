#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node * left;
	struct node * right;
};

struct node * newNode (int num) {
	struct node* temp = (struct node*) malloc (sizeof(struct node));
	temp->data = num;
	temp->left = temp->right = NULL;
	return temp;
}

struct node * insert (struct node* temp, int data) {
	if (temp == NULL) {
		return newNode(data);
	}
	if (temp->data >= data) {
		temp->left = insert(temp->left, data);
	} else {
		temp->right = insert(temp->right, data);
	}
	return temp;
}

void inOrder (struct node* root) {
	if (root != NULL) {
		inOrder(root->left);
		printf ("%d\t", root->data);
		inOrder(root->right);
	}
}

void modifyBSTUtil (struct node* root, int *sum) {
	if (root == NULL) {
		return;
	}
	modifyBSTUtil (root->right, sum);
	*sum = *sum + root->data;
	root->data = *sum;
	modifyBSTUtil (root->left, sum);
}

void modifyBST (struct node* root) {
	int sum = 0;
	modifyBSTUtil (root, &sum);
}

int main (void) {
	struct node* root = NULL;
	root = insert(root, 50);
	insert(root, 30);
	insert(root, 20);
	insert(root, 40);
	insert(root, 70);
	insert(root, 60);
	insert(root, 80);
	modifyBST(root);
	inOrder(root);
	return 0;
}
