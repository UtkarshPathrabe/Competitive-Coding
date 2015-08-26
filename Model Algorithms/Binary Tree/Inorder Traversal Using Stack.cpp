#include <bits/stdc++.h>

using namespace std;

struct tNode {
	int data;
	struct tNode* left;
	struct tNode* right;
};

struct sNode {
	struct tNode* t;
	struct sNode* next;
};

struct tNode* newNode(int num) {
	struct tNode* temp = (struct tNode*)malloc(sizeof(struct tNode));
	temp->data = num;
	temp->left = NULL;
	temp->right = NULL;
	return temp;
}

void push (struct sNode** top, struct tNode* temp) {
	struct sNode* node = (struct sNode*)malloc(sizeof(struct sNode));
	if (node == NULL) {
		printf("Stack Overflow");
		exit(0);
	}
	node->t = temp;
	node->next = *top;
	*top = node;
}

int isEmpty (struct sNode *top) {
	if (top == NULL) {
		return 1;
	} else {
		return 0;
	}
}

struct tNode* pop (struct sNode **top_ref) {
	struct sNode* top;
	struct tNode* s;
	if (isEmpty(*top_ref)) {
		printf ("Stack Underflow");
		exit(0);
	} else {
		top = *top_ref;
		s = top->t;
		*top_ref = top->next;
		free(top);
		return s;
	}
}

void inOrder (struct tNode* root) {
	struct sNode* s = NULL;
	struct tNode* current = root;
	int done = 0;
	while (!done) {
		if (current != NULL) {
			push (&s, current);
			current = current->left;
		} else {
			if (!isEmpty(s)) {
				current = pop(&s);
				printf("%d\t", current->data);
				current = current->right;
			} else {
				done = 1;
			}
		}
	}
}

int main (void) {
	struct tNode* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->left = newNode(4);
	root->left->right = newNode(5);
	inOrder(root);
	return 0;
}
