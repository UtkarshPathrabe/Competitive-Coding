/* Time Complexity: O(Log(N)) for Insertion and Deletion */

#include <bits/stdc++.h>

using namespace std;

struct node {
	int key;
	int height;
	int count;
	struct node* left;
	struct node* right;
};

int max (int a, int b) {
	return (a > b) ? a : b;
}

int height (struct node* root) {
	if (root == NULL) {
		return 0;
	} else {
		return root->height;
	}
}

struct node* newNode (int key) {
	struct node* temp = (struct node*) malloc (sizeof (struct node));
	temp->key = key;
	temp->left = NULL;
	temp->right = NULL;
	temp->height = 1;
	temp->count = 1;
	return temp;
}

struct node* rightRotate (struct node* y) {
	struct node* x = y->left;
	struct node* T2 = x->right;
	x->right = y;
	y->left = T2;
	y->height = max (height (y->left), height (y->right)) + 1;
	x->height = max (height (x->left), height (x->right)) + 1;
	return x;
}

struct node* leftRotate (struct node* x) {
	struct node* y = x->right;
	struct node* T2 = y->left;
	y->left = x;
	x->right = T2;
	x->height = max (height (x->left), height (x->right)) + 1;
	y->height = max (height (y->left), height (y->right)) + 1;
	return y;
}

int getBalance (struct node* root) {
	if (root == NULL) {
		return 0;
	} else {
		return (height (root->left) - height (root->right));
	}
}

struct node* insert (struct node* node, int key) {
	if (node == NULL) {
		return newNode (key);
	}
	if (key == node->key) {
		(node->count)++;
		return node;
	}
	if (key < node->key) {
		node->left = insert (node->left, key);
	} else {
		node->right = insert (node->right, key);
	}
	node->height = max (height (node->left), height (node->right)) + 1;
	int balance = getBalance (node);
	if ((balance > 1) && (key < node->left->key)) {
		return rightRotate (node);
	}
	if ((balance < -1) && (key > node->right->key)) {
		return leftRotate (node);
	}
	if ((balance > 1) && (key > node->left->key)) {
		node->left = leftRotate (node->left);
		return rightRotate (node);
	}
	if ((balance < -1) && (key < node->right->key)) {
		node->right = rightRotate (node->right);
		return leftRotate (node);
	}
	return node;
}

struct node* minValueNode (struct node* node) {
	struct node* curr = node;
	while (curr->left) {
		curr = curr->left;
	}
	return curr;
}

struct node* deleteNode (struct node* root, int key) {
	if (root == NULL) {
		return NULL;
	}
	if (key < root->key) {
		root->left = deleteNode (root->left, key);
	} else if (key > root->key) {
		root->right = deleteNode (root->right, key);
	} else {
		if (root->count > 1) {
			(root->count)--;
			return root;
		}
		if ((root->left == NULL) || (root->right == NULL)) {
			struct node* temp = (root->left ? root->left : root->right);
			if (temp == NULL) {
				temp = root;
				root = NULL;
			} else {
				*root = *temp;
			}
			free (temp);
		} else {
			struct node* temp = minValueNode (root->right);
			root->key = temp->key;
			root->right = deleteNode (root->right, temp->key);
		}
	}
	if (root == NULL) {
		return NULL;
	}
	root->height = max (height (root->left), height (root->right)) + 1;
	int balance = getBalance (root);
	if ((balance > 1) && (getBalance (root->left) >= 0)) {
		return rightRotate (root);
	}
	if ((balance > 1) && (getBalance (root->left) < 0)) {
		root->left = leftRotate (root->left);
		return rightRotate (root);
	}
	if ((balance < -1) && (getBalance (root->right) <= 0)) {
		return leftRotate (root);
	}
	if ((balance < -1) && (getBalance (root->right) > 0)) {
		root->right = rightRotate (root->right);
		return leftRotate (root);
	}
	return root;
}

void preOrder (struct node* root) {
	if (root != NULL) {
		cout << root->key << "(" << root->count << ")\t";
		preOrder (root->left);
		preOrder (root->right);
	}
}

int main (void) {
	struct node *root = NULL;
	root = insert (root, 9);
    root = insert (root, 5);
    root = insert (root, 10);
    root = insert (root, 0);
    root = insert (root, 6);
    root = insert (root, 11);
    root = insert (root, -1);
    root = insert (root, 1);
    root = insert (root, 2);
    root = insert (root, 9);
    /* The constructed AVL Tree would be
            9
           /  \
          1    10
        /  \     \
       0    5     11
      /    /  \
     -1   2    6						*/
	cout << "Pre Order Traversal of the constructed AVL Tree is:" << endl;
	preOrder (root);
	cout << endl;
	root = deleteNode (root, 10);
    /* The AVL Tree after deletion of 10
            1
           /  \
          0    9
        /     /  \
       -1    5     11
           /  \
          2    6						*/
    cout << "Pre order traversal after deletion of 10 is:" << endl;
    preOrder(root);
    cout << endl;
    root = deleteNode (root, 9);
    cout << "Pre order traversal after deletion of 9 is:" << endl;
    preOrder(root);
    cout << endl;
	return 0;
}
