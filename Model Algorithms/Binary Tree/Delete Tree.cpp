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

void deleteTree(struct node* temp) {
	if (temp == NULL) {
		return;
	}
	deleteTree(temp->left);
	deleteTree(temp->right);
	printf("Deleting %d Node\n", temp->data);
	free(temp);
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	deleteTree(root);
	printf ("Whole tree deleted.\n");
	return 0;
}
