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

int getLevel (struct node* temp, int data, int level) {
	if (temp == NULL) {
		return 0;
	}
	if (temp->data == data) {
		return level;
	}
	int newLevel = getLevel(temp->left, data, level+1);
	if (newLevel != 0) {
		return newLevel;
	}
	newLevel = getLevel(temp->right, data, level+1);
	return newLevel;
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	root->right->right = newNode(7);
	int node = 4;
	printf("The level of node %d is %d.\n", node, getLevel(root, node, 1));
	return 0;
}
