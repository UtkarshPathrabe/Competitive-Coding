//Time Complexity : O(n*log(n))

#include <bits/stdc++.h>

using namespace std;

struct MinHeapNode {
	char data;
	unsigned int freq;
	struct MinHeapNode *left, *right;
};

struct MinHeap {
	unsigned int size, capacity;
	struct MinHeapNode **array;
};

struct MinHeapNode *newNode (char data, unsigned int freq) {
	struct MinHeapNode *temp = (struct MinHeapNode *) malloc (sizeof(struct MinHeapNode));
	temp->left = temp->right = NULL;
	temp->data = data;
	temp->freq = freq;
	return temp;
}

struct MinHeap *createMinHeap (unsigned int capacity) {
	struct MinHeap* temp = (struct MinHeap*) malloc (sizeof (struct MinHeap));
	temp->size = 0;
	temp->capacity = capacity;
	temp->array = (struct MinHeapNode**) malloc (temp->capacity * sizeof(struct MinHeapNode*));
	return temp;
}

void swapMinHeapNode (struct MinHeapNode **a, struct MinHeapNode **b) {
	struct MinHeapNode *temp = *a;
	*a = *b;
	*b = temp;
}

void minHeapify (struct MinHeap *minHeap, int idx) {
	int smallest = idx;
	int left = 2*idx + 1;
	int right = 2*idx + 2;
	if ((left < minHeap->size) && (minHeap->array[left]->freq < minHeap->array[smallest]->freq)) {
		smallest = left;
	}
	if ((right < minHeap->size) && (minHeap->array[right]->freq < minHeap->array[smallest]->freq)) {
		smallest = right;
	}
	if (smallest != idx) {
		swapMinHeapNode (&minHeap->array[idx], &minHeap->array[smallest]);
		minHeapify (minHeap, smallest);
	}
}

void buildMinHeap (struct MinHeap* minHeap) {
	int n = minHeap->size - 1;
	for (int i = (n-1)/2; i >= 0; i--) {
		minHeapify (minHeap, i);
	}
}

struct MinHeap* createAndBuildMinHeap (char data[], unsigned int freq[], unsigned int size) {
	struct MinHeap* temp = createMinHeap (size);
	for (int i = 0; i < size; i++) {
		temp->array[i] = newNode (data[i], freq[i]);
	}
	temp->size = size;
	buildMinHeap (temp);
	return temp;
}

struct MinHeapNode *extractMin (struct MinHeap* minHeap) {
	struct MinHeapNode *temp = minHeap->array[0];
	minHeap->array[0] = minHeap->array[--minHeap->size];
	minHeapify (minHeap, 0);
	return temp;
}

void insertMinHeap (struct MinHeap *minHeap, struct MinHeapNode* minHeapNode) {
	int i = minHeap->size++;
	while (i && minHeapNode->freq < minHeap->array[(i-1)/2]->freq) {
		minHeap->array[i] = minHeap->array[(i-1)/2];
		i = (i-1)/2;
	}
	minHeap->array[i] = minHeapNode;
}

int isSizeOne (struct MinHeap *temp) {
	return (temp->size == 1);
}

int isLeaf (struct MinHeapNode *temp) {
	return (!(temp->left) && !(temp->right));
}

void printArr (int arr[], int n) {
	for (int i = 0; i < n; i++) {
		cout << arr[i];
	}
	cout << endl;
}

int height (struct MinHeapNode *root) {
	if (root == NULL) {
		return 0;
	} else {
		return max(height(root->left), height(root->right)) + 1;
	}
}

struct MinHeapNode* buildHuffmanTree (char data[], unsigned int freq[], unsigned int size) {
	struct MinHeapNode *left, *right, *top;
	struct MinHeap *minHeap = createAndBuildMinHeap (data, freq, size);
	while (!isSizeOne (minHeap)) {
		left = extractMin (minHeap);
		right = extractMin (minHeap);
		top = newNode ('$', left->freq + right->freq);
		top->left = left;
		top->right = right;
		insertMinHeap (minHeap, top);
	}
	return extractMin (minHeap);
}

void printCodes (struct MinHeapNode* root, int arr[], int top) {
	if (root->left) {
		arr[top] = 0;
		printCodes (root->left, arr, top+1);
	}
	if (root->right) {
		arr[top] = 1;
		printCodes (root->right, arr, top+1);
	}
	if (isLeaf (root)) {
		cout << root->data << "\t\t->\t";
		printArr (arr, top);
	}
}

void HuffmanCodes (char data[], unsigned int freq[], unsigned int size) {
	struct MinHeapNode* root = buildHuffmanTree (data, freq, size);
	cout << "Huffman Tree construction done." << endl << "Printing Huffman Codes for alphabets:" << endl << "Alphabet\t\tCode" << endl;
	int arr[height(root)+1], top = 0;
	printCodes (root, arr, top);
}

int main (void) {
	char data[] = {'a', 'b', 'c', 'd', 'e', 'f'};
	unsigned int freq[] = {5, 9, 12, 13, 16, 45};
	unsigned int size = sizeof (data) / sizeof (data[0]);
	HuffmanCodes (data, freq, size);
	return 0;
}
