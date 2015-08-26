#include <bits/stdc++.h>

using namespace std;

struct lNode {
	int data;
	struct lNode* next;
};

struct tNode {
	int data;
	struct node* left;
	struct node* right;
};

struct tNode* newNode(int num) {
	struct tNode* temp = (struct node*)malloc(sizeof(struct node));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

void push(struct lNode** head_ref, int data) {
	struct lNode* temp = (struct lNode*)malloc(sizeof(struct lNode));
	temp->data = data;
	temp->next = *head;
	*head = temp;
}

int main (void) {
	
	return 0;
}
