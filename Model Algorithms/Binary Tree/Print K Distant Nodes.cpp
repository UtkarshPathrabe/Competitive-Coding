#include <bits/stdc++.h>

using namespace std;

struct node{
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

void printKDistant(struct node* temp, int k) {
	if (temp == NULL) {
		return;
	}
	if (k == 0) {
		printf ("%d\t", temp->data);
	} else if (k > 0) {
		printKDistant(temp->left, k-1);
		printKDistant(temp->right, k-1);
	}
}

int main(void){
	struct node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	root->right->left = newNode(6);
	root->right->right = newNode(7);
	printKDistant(root, 2);
	return 0;
}
