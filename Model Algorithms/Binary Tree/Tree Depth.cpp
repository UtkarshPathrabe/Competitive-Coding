#include <bits/stdc++.h>
#define max(a, b) {(a > b) ? a : b}

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

int treeDepth(struct node* temp) {
	if (temp == NULL) {
		return 0;
	} else {
		return ((treeDepth(temp->left) > treeDepth(temp->right)) ? (treeDepth(temp->left) + 1) : (treeDepth(temp->right) + 1));
	}
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	printf ("Height of the tree is %d\n", treeDepth(root));
	return 0;
}
