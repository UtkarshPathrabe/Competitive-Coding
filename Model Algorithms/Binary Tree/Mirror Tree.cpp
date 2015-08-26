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

void treeMirror (struct node* temp) {
	if (temp == NULL) {
		return;
	}
	treeMirror(temp->left);
	treeMirror(temp->right);
	struct node* t = temp->left;
	temp->left = temp->right;
	temp->right = t;
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

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	treeMirror (root);
	printf ("Printing InOrder Traversal:\n");
	printInOrder (root);
	printf ("\n");
	return 0;
}
