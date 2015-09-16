#include <bits/stdc++.h>

using namespace std;

struct node {
	int data;
	struct node* npx;
};

struct node* XOR (struct node* a, struct node* b) {
	return (struct node*) ((uintptr_t)(a) ^ (uintptr_t)(b));
}

void insert (struct node** head_ref, int data) {
	struct node* temp = (struct node*) malloc (sizeof (struct node));
	temp->data = data;
	temp->npx = XOR (*head_ref, NULL);
	if (*head_ref != NULL) {
		struct node* next = XOR ((*head_ref)->npx, NULL);
		(*head_ref)->npx = XOR (temp, next);
	}
	*head_ref = temp;
}

void printList (struct node* head) {
	struct node* curr = head;
	struct node* prev = NULL;
	struct node* next = NULL;
	cout << "The Nodes of Linked List are:" << endl;
	while (curr != NULL) {
		cout << curr->data << "\t";
		next = XOR (prev, curr->npx);
		prev = curr;
		curr = next;
	}
	cout << endl;
}

int main (void) {
	struct node *head = NULL;
	insert (&head, 10);
	insert (&head, 20);
	insert (&head, 30);
	insert (&head, 40);
	printList (head);
	return 0;
}
