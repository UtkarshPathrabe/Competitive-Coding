#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node *left;
	struct node *right;
};

struct node* newNode (int num) {
	struct node* temp = (struct node*) malloc(sizeof(struct node));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

void printPreOrder (struct node* temp) {
	if (temp == NULL) {
		return;
	} else {
		printf("%d\t", temp->data);
		printPreOrder (temp->left);
		printPreOrder (temp->right);
	}
}

void printPostOrder (struct node* temp) {
	if (temp == NULL) {
		return;
	} else {
		printPostOrder (temp->left);
		printPostOrder (temp->right);
		printf ("%d\t", temp->data);
	}
}

void printInOrder (struct node* temp) {
	if (temp == NULL) {
		return;
	} else {
		printInOrder (temp->left);
		printf ("%d\t", temp->data);
		printInOrder (temp->right);
	}
}

int treeSize (struct node* temp) {
	if (temp == NULL) {
		return 0;
	} else {
		return treeSize(temp->left) + treeSize(temp->right) + 1;
	}
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	printf ("Printing InOrder Traversal:\n");
	printInOrder (root);
	printf ("\n");
	printf ("Printing PreOrder Traversal:\n");
	printPreOrder (root);
	printf ("\n");
	printf ("Printing PostOrder Traversal:\n");
	printPostOrder (root);
	printf ("\n");
	printf ("The Size of the Tree is %d.\n", treeSize(root));
	return 0;
}
