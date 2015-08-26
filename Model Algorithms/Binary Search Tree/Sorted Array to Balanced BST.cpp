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

struct node* arrayToBST (int arr[], int start, int end) {
	if (start > end) {
		return NULL;
	}
	int mid = (start + end) / 2;
	struct node* temp = newNode(arr[mid]);
	temp->left = arrayToBST (arr, start, mid - 1);
	temp->right = arrayToBST (arr, mid + 1, end);
	return temp;
}

void printPreOrder (struct node* temp) {
	if (temp != NULL) {
		printf ("%d\t", temp->data);
		printPreOrder(temp->left);
		printPreOrder(temp->right);
	}
}

int main (void) {
	int arr[] = {1,2,3,4,5,6,7};
	int n = sizeof(arr)/sizeof(arr[0]);
	struct node* root = arrayToBST (arr, 0, n-1);
	printf ("Pre Order Traversal of tree is:\n");
	printPreOrder (root);
	return 0;
}
