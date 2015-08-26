#include <bits/stdc++.h>

using namespace std;

struct node {
    char data;
    struct node* left;
    struct node* right;       
};

struct node* newNode (char c) {
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = c;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

int search(char arr[], int start, int end, char data) {
    for (int i = start; i <= end; i++) {
        if (arr[i] == data) {
            return i;
        }
    }
    return -1;
}

struct node* buildTree(char in[], char pre[], int start, int end) {
    if (start > end) {
        return NULL;
    }
    static int preIndex = 0;
    struct node* temp = newNode(pre[preIndex++]);
    int index = search(in, start, end, temp->data);
    temp->left = buildTree(in, pre, start, index - 1);
    temp->right = buildTree(in, pre, index + 1, end);
    return temp;
}

void printInOrder(struct node* temp) {
    if (temp == NULL) {
        return;
    }
    printInOrder(temp->left);
    printf("%c\t", temp->data);
    printInOrder(temp->right);
}

int main (void) {
    char in[] = {'D', 'B', 'E', 'A', 'F', 'C'};
    char pre[] = {'A', 'B', 'D', 'E', 'C', 'F'};
    int len = sizeof(in)/sizeof(in[0]);
    struct node* root = buildTree(in, pre, 0, len - 1);
    printf ("Inorder traversal of the build tree:\n");
    printInOrder(root);
    printf("\n");
    return 0;
}
