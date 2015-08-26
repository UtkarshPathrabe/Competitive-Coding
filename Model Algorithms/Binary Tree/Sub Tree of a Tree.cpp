#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node* left;
	struct node* right;
};

struct node* newNode(int num) {
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

int areIdentical(struct node* T, struct node* S) {
	if (T == NULL && S == NULL) {
		return 1;
	}
	if (T == NULL || S == NULL) {
		return 0;
	}
	if ((T->data == S->data) && (areIdentical(T->left, S->left)) && (areIdentical(T->right, S->right))) {
		return 1;
	} else {
		return 0;
	}
}

int isSubTree (struct node* T, struct node* S) {
	if (S == NULL) {
		return 1;
	}
	if (T == NULL) {
		return 0;
	}
	if (areIdentical(T, S)) {
		return 1;
	}
	return (isSubTree(T->left, S) || isSubTree(T->right, S));
}

int main (void) {
	struct node* T = newNode(26);
	T->left = newNode(10);
	T->right = newNode(3);
	T->left->left = newNode(4);
	T->left->left->right = newNode(30);
	T->left->right = newNode(6);
	T->right->right = newNode(3);
	struct node* S = newNode(10);
	S->right = newNode(6);
	S->left = newNode(4);
	S->left->right = newNode(30);
	if (isSubTree(T, S)) {
		printf("Tree S is subtree of tree T.\n");
	} else {
		printf("Tree S is not a subtree of tree T.\n");
	}
	return 0;
}
