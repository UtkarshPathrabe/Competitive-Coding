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

void inOrder (struct node* temp) {
	if (temp == NULL) {
		return;
	}
	inOrder(temp->left);
	printf("%d\t", temp->data);
	inOrder(temp->right);
}

struct node* constructBSTUtil (int pre[], int *preIndex, int key, int min, int max, int size) {
	if (*preIndex >= size) {
		return NULL;
	}
	struct node* root = NULL;
	if (key > min && key < max) {
		root = newNode(key);
		*preIndex = *preIndex + 1;
		if (*preIndex < size) {
			root->left = constructBSTUtil(pre, preIndex, pre[*preIndex], min, key, size);
			root->right = constructBSTUtil(pre, preIndex, pre[*preIndex], key, max, size);
		}
	}
	return root;
}

struct node* constructBST (int pre[], int size) {
	int preIndex = 0;
	return constructBSTUtil(pre, &preIndex, pre[0], INT_MIN, INT_MAX, size);
}

int main (void) {
	int pre[] = {10, 5, 1, 7, 40, 50};
	int size = sizeof(pre) / sizeof(pre[0]);
	struct node *root = constructBST(pre, size);
	printf("Inorder traversal of the constructed tree:\n");
	inOrder(root);
	return 0;
}
