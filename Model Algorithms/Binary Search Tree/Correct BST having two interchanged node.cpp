#include <bits/stdc++.h>

using namespace std;

struct node{
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

struct node* insert (struct node* root, int data) {
	if (root == NULL) {
		return newNode(data);
	}
	if (data <= root->data) {
		root->left = insert(root->left, data);
	} else {
		root->right = insert(root->right, data);
	}
	return root;
}

void inOrder (struct node* temp) {
	if (temp == NULL) {
		return;
	}
	inOrder(temp->left);
	printf("%d\t", temp->data);
	inOrder(temp->right);
}

void swap (int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void correctBSTUtil (struct node* root, struct node** first, struct node** middle, struct node** last, struct node** prev) {
	if (root == NULL) {
		return;
	}
	correctBSTUtil (root->left, first, middle, last, prev);
	if ((*prev) && (root->data < (*prev)->data)) {
		if (*first) {
			*last = root;
		} else {
			*first = *prev;
			*middle = root;
		}
	}
	*prev = root;
	correctBSTUtil (root->right, first, middle, last, prev);
}

void correctBST (struct node* root) {
	if (root == NULL) {
		return;
	}
	struct node* first = NULL;
	struct node* middle = NULL;
	struct node* last = NULL;
	struct node* prev = NULL;
	correctBSTUtil (root, &first, &middle, &last, &prev);
	if (first && last) {
		swap (&(first->data), &(last->data));
	} else if (first && middle) {
		swap (&(first->data), &(middle->data));
	}
}

int main (void) {
	struct node* root = newNode(6);
	root->left = newNode(10);
	root->right = newNode(2);
	root->left->left = newNode(1);
	root->left->right = newNode(3);
	root->right->right = newNode(12);
	root->right->left = newNode(7);
	printf("Inorder Traversal of the original tree:\n");
	inOrder (root);
	correctBST (root);
	printf("\nInorder Traversal of the fixed tree:\n");
	inOrder (root);
	return 0;
}
