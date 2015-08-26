#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node* left;
	struct node* right;
};

int sameTrees (struct node* temp1, struct node *temp2) {
	if ((temp1 == NULL) && (temp2 == NULL)) {
		return 1;
	} else if ((temp1 != NULL) && (temp2 != NULL)) {
		return (sameTrees(temp1->left, temp2->left) && sameTrees(temp1->right, temp2->right) && (temp1->data == temp2->data));
	}
	return 0;
}

struct node* newNode (int num) {
	struct node* temp = (struct node*)malloc(sizeof(struct node));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

int main (void) {
	struct node* root1 = newNode(1);
	root1->left = newNode(2);
	root1->right = newNode(3);
	root1->left->left = newNode(4);
	root1->left->right = newNode(5);
	struct node* root2 = newNode(1);
	root2->left = newNode(2);
	root2->right = newNode(3);
	root2->left->left = newNode(4);
	root2->left->right = newNode(5);
	struct node* root3 = newNode(1);
	root3->left = newNode(2);
	root3->right = newNode(3);
	root3->left->left = newNode(4);
	root3->left->right = newNode(6);
	if (sameTrees(root1, root2)) {
		printf("Tree1 and Tree2 are identical.\n");
	} else {
		printf("Tree1 and Tree2 are not identical.\n");
	}
	if (sameTrees(root1, root3)) {
		printf("Tree1 and Tree3 are identical.\n");
	} else {
		printf("Tree1 and Tree3 are not identical.\n");
	}
	return 0;
}
