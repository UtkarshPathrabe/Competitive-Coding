#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node* left;
	struct node* right;
};

struct node* newNode (int num) {
	struct node* temp = (struct node*) malloc (sizeof(struct node));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

// It is assumed that n1 < n2
void printBetween (struct node* temp, int n1, int n2) {
	if (temp == NULL) {
		return;
	}
	if (temp->data > n1) {
		printBetween(temp->left, n1, n2);
	}
	if (temp->data >= n1 && temp->data <= n2) {
		printf ("%d\t", temp->data);
	}
	if (temp->data < n2) {
		printBetween(temp->right, n1, n2);
	}
}

int main(void) {
	int n1 = 10, n2 = 25;
	struct node* root = newNode(20);
	root->left = newNode(8);
	root->right = newNode(22);
	root->left->left = newNode(4);
	root->left->right = newNode(12);
	printBetween(root, n1, n2);
	return 0;
}
