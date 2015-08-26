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
	temp->nextRight = NULL;
	return temp;
}

struct node* getNextRight(struct node* temp) {
	struct node* p = temp;
	while (temp != NULL) {
		if (temp->left) {
			return temp->left;
		}
		if (temp->right) {
			return temp->right;
		}
		temp = temp->nextRight; 
	}
	return NULL;
}

void connect (struct node* p) {
	
}

int main (void) {
	
	return 0;
}
