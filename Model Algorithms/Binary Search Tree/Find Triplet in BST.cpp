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

void convertBSTtoDLL (struct node* temp, struct node** head, struct node** tail) {
	if (temp == NULL) {
		return;
	}
	if (temp->left) {
		convertBSTtoDLL(temp->left, head, tail);
	}
	temp->left = *tail;
	if (*tail) {
		(*tail)->right = temp;
	} else {
		*head = temp;
	}
	*tail = temp;
	if (temp->right) {
		convertBSTtoDLL(temp->right, head, tail);
	}
}

int isPresentInDLL (struct node* head, struct node* tail, int sum) {
	while (head != tail) {
		int curr = head->data + tail->data;
		if (curr == sum) {
			return 1;
		} else if (curr > sum) {
			tail = tail->left;
		} else {
			head = head->right;
		}
	}
	return 0;
}

int isTripletPresent (struct node* root) {
	if (root == NULL) {
		return 0;
	}
	struct node* head = NULL;
	struct node* tail = NULL;
	convertBSTtoDLL (root, &head, &tail);
	while ((head->right != tail) && (head->data < 0)) {
		if (isPresentInDLL(head->right, tail, -1*(head->data))) {
			return 1;
		} else {
			head = head->right;
		}
	}
	return 0;
}

int main (void) {
	struct node* root = NULL;
	root = insert(root, 6);
	root = insert(root, -13);
	root = insert(root, 14);
	root = insert(root, -8);
	root = insert(root, 15);
	root = insert(root, 13);
	root = insert(root, 7);
	if (isTripletPresent(root)) {
		printf("Present.\n");
	} else {
		printf("Not Present.\n");
	}
	return 0;
}
