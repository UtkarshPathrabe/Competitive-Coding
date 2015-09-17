#include <bits/stdc++.h>

using namespace std;

struct node {
	int key;
	struct node *left, *right;
};

struct node* newNode (int key) {
	struct node* node = (struct node*) malloc (sizeof (struct node));
	node->key = key;
	node->left = node->right = NULL;
	return node;
}

struct node* rightRotate (struct node* x) {
	struct node* y = x->left;
	x->left = y->right;
	y->right = x;
	return y;
}

struct node* leftRotate (struct node* x) {
	struct node* y = x->right;
	x->right = y->left;
	y->left = x;
	return y;
}

struct node* splay (struct node* root, int key) {
	if ((root == NULL) || (root->key == key)) {
		return root;
	}
	if (key < root->key) {
		if (root->left == NULL) {
			return root;
		}
		if (root->left->key > key) {
			root->left->left = splay (root->left->left, key);
			root = rightRotate (root);
		} else if (root->left->key < key) {
			root->left->right = splay (root->left->right, key);
			if (root->left->right != NULL) {
				root->left = leftRotate (root->left);
			}
		}
		return (root->left == NULL) ? root : rightRotate (root);
	} else {
		if (root->right == NULL) {
			return root;
		}
		if (root->right->key > key) {
			root->right->left = splay (root->right->left, key);
			if (root->right->left != NULL) {
				root->right = rightRotate (root->right);
			}
		} else if (root->right->key < key) {
			root->right->right = splay (root->right->right, key);
			root = leftRotate (root);
		}
		return (root->right == NULL) ? root : leftRotate (root);
	}
}

struct node* search (struct node* root, int key) {
	return splay (root, key);
}

struct node* insert (struct node* root, int key) {
	if (root == NULL) {
		return newNode (key);
	}
	root = splay (root, key);
	if (root->key == key) {
		return root;
	}
	struct node* node = newNode (key);
	if (root->key > key) {
		node->right = root;
		node->left = root->left;
		root->left = NULL;
	} else {
		node->left = root;
		node->right = root->right;
		root->right = NULL;
	}
	return node;
}

void preOrder (struct node* root) {
	if (root != NULL) {
		cout << root->key << "\t";
		preOrder (root->left);
		preOrder (root->right);
	}
}

int main (void) {
	struct node *root = newNode(100);
    root->left = newNode(50);
    root->right = newNode(200);
    root->left->left = newNode(40);
    root->left->left->left = newNode(30);
    root->left->left->left->left = newNode(20);
    root = search(root, 20);
    cout << "Preorder traversal of the modified Splay tree is:" << endl;
    preOrder(root);
    cout << endl;
    root = search(root, 100);
    cout << "Preorder traversal of the modified Splay tree is:" << endl;
    preOrder(root);
    cout << endl;
    root = insert(root, 25);
    cout << "Preorder traversal of the modified Splay tree is:" << endl;
    preOrder(root);
    cout << endl;
	return 0;
}
