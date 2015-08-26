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

void printPathRecur (struct node* temp, int path[], int len) {
	if (temp == NULL)
		return;
	path[len++] = temp->data;
	if (temp->left == NULL && temp->right == NULL) {
		for (int i = 0; i < len; i++) {
			printf("%d\t", path[i]);
		}
		printf("\n");
	} else {
		printPathRecur (temp->left, path, len);
		printPathRecur (temp->right, path, len);
	}
}

void printPath (struct node* temp) {
	int path[10] = {0};
	printPathRecur(temp, path, 0);
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	printPath(root);
	return 0;
}
