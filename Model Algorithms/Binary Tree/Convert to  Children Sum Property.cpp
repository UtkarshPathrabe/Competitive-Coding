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

void increment (struct node* temp, int diff) {
	if (temp->left != NULL) {
		temp->left->data += diff;
		increment(temp->left, diff);
	} else if (temp->right != NULL) {
		temp->right->data += diff;
		increment(temp->right, diff);
	}
}

void convertChildrenSum (struct node* temp) {
	if ((temp == NULL) || (temp->left == NULL && temp->right == NULL)) {
		return;
	} else {
		convertChildrenSum (temp->left);
		convertChildrenSum (temp->right);
		int l = 0, r = 0, diff;
		if (temp->left != NULL) {
			l = temp->left->data;
		}
		if (temp->right != NULL) {
			r = temp->right->data;
		}
		diff = (l + r) - (temp->data);
		if (diff > 0) {
			temp->data += diff;
		} else if (diff < 0) {
			increment(temp, -diff);
		}
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

int main (void) {
	struct node* root = newNode(50);
	root->left = newNode(7);
	root->right = newNode(2);
	root->left->left = newNode(3);
	root->left->right = newNode(5);
	root->right->left = newNode(1);
	root->right->right = newNode(30);
	printf("Inorder traversal before conversion:\n");
	printInOrder (root);
	convertChildrenSum(root);
	printf("\nInorder traversal after conversion:\n");
	printInOrder (root);
	printf("\n");
	return 0;
}
