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

int treeDepth(struct node* temp) {
	if (temp == NULL) {
		return 0;
	} else {
		return ((treeDepth(temp->left) > treeDepth(temp->right)) ? (treeDepth(temp->left) + 1) : (treeDepth(temp->right) + 1));
	}
}

void printGivenLevel (struct node* temp, int level) {
	if (temp == NULL) {
		return;
	}
	if (level == 1) {
		printf ("%d\t", temp->data);
	} else if (level > 1) {
		printGivenLevel(temp->left, level-1);
		printGivenLevel(temp->right, level-1);
	}
}

void printLevelOrder (struct node* temp) {
	int h = treeDepth(temp);
	for (int i = 1; i <= h; i++) {
		printGivenLevel(temp, i);
	}
}

int main (void) {
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	printLevelOrder(root);
	return 0;
}
