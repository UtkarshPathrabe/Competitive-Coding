/* Author: Utkarsh Ashok Pathrabe
*  Algorithm: Huffman Encoding
*/

/* Time Complexity: O(n*log(n)) where n is the number of unique characters. If there are n nodes, ExtractMin() is called 2*(n-1) times, 
*  ExtractMin() takes O(log(n)) time as it calls MinHeapify(). */

#include <bits/stdc++.h>

using namespace std;

struct _node {									// Huffman tree node
	char data;									// Data to be stored
	int freq;									// Frequency of Data
	struct _node *left, *right;					// Left and Right child pointers
};
typedef struct _node * Node;					// Pointer to Node

Node NewNode (char data, int freq) {						// Utility function to allocate a node with given data and its frequency
	Node temp = (Node) malloc (sizeof (struct _node));		// Assign memory to Node
	temp -> data = data;									// Assign data to Node
	temp -> freq = freq;									// Assign frequency to Node
	temp -> left = temp -> right = NULL;					// Initialize left and right child pointers to  NULL
	return temp;
}

struct _minHeap {								// Min Heap: Collection of Huffman Tree Nodes
	unsigned int size;							// Current Size of Min Heap
	unsigned int capacity;						// Capacity of Min Heap
	Node * Array;								// Array of Min Heap Node Pointers
};
typedef struct _minHeap * MinHeap;				// Pointer to Min Heap

MinHeap CreateMinHeap (unsigned int capacity) {										// Utility function to create a Min Heap of Given Capacity
	MinHeap minheap = (MinHeap) malloc (sizeof (struct _minHeap));					// Assign memory to Min Heap
	minheap -> size = 0;															// Current Size is zero
	minheap -> capacity = capacity;													// Initialize capacity of Min Heap
	minheap -> Array = (Node *) malloc (sizeof (struct _node) * capacity);			// Assign memory to array of Nodes
	return minheap;
}

void SwapNode (Node * a, Node * b) {
	Node t = *a;
	*a = *b;
	*b = t;
}

void MinHeapify (MinHeap minheap, int index) {
	int smallest = index, left = ((2 * index) + 1), right = ((2 * index) + 2);
	if ((left < minheap -> size) && ((minheap -> Array[left] -> freq) < (minheap -> Array[smallest] -> freq))) {
		smallest = left;
	}
	if ((right < minheap -> size) && ((minheap -> Array[right] -> freq) < (minheap -> Array[smallest] -> freq))) {
		smallest = right;
	}
	if (smallest != index) {
		SwapNode (&minheap -> Array[smallest], &minheap -> Array[index]);
		MinHeapify (minheap, smallest);
	}
}

bool IsSizeOne (MinHeap minheap) {
	return (minheap -> size == 1);
}

bool IsLeaf (Node node) {
	return (!(node -> left) && !(node -> right));
}

Node ExtractMin (MinHeap minheap) {
	Node temp = minheap -> Array[0];
	minheap -> Array[0] = minheap -> Array[--(minheap -> size)];
	MinHeapify (minheap, 0);
	return temp;
}

void InsertMinHeap (MinHeap minheap, Node node) {
	int i = (minheap -> size)++;
	while (i && ((node -> freq) < (minheap -> Array[(i - 1) / 2] -> freq))) {
		minheap -> Array[i] = minheap -> Array[(i - 1) / 2];
		i = (i - 1) / 2;
	}
	minheap -> Array[i] = node;
}

void BuildMinHeap (MinHeap minheap) {
	for (int i = (((minheap -> size) - 1) / 2); i >= 0; i--) {
		MinHeapify (minheap, i);
	}
}

void PrintArray (int array[], int size) {
	for (int i = 0; i < size; i++) {
		cout << array[i];
	}
}

MinHeap CreateAndBuildMinHeap (char data[], int freq[], int size) {
	MinHeap minheap = CreateMinHeap (size);
	for (int i = 0; i < size; i++) {
		minheap -> Array[i] = NewNode (data[i], freq[i]);
	}
	minheap -> size = size;
	BuildMinHeap (minheap);
	return minheap;
}

Node BuildHuffmanTree (char data[], int freq[], int size) {
	Node left, right, newNode;
	MinHeap minheap = CreateAndBuildMinHeap (data, freq, size);
	while (!IsSizeOne (minheap)) {
		left = ExtractMin (minheap);
		right = ExtractMin (minheap);
		newNode = NewNode ('$', (left -> freq) + (right -> freq));
		newNode -> left = left;
		newNode -> right = right;
		InsertMinHeap (minheap, newNode);
	}
	return ExtractMin (minheap);
}

void PrintCodes (Node node, int array[], int index) {
	if (node -> left) {
		array[index] = 0;
		PrintCodes (node -> left, array, index + 1);
	}
	if (node -> right) {
		array[index] = 1;
		PrintCodes (node -> right, array, index + 1);
	}
	if (IsLeaf (node)) {
		cout << node -> data << " :\t";
		PrintArray (array, index);
		cout << endl;
	}
}

void HuffmanEncode (char data[], int freq[], int size) {
	Node root = BuildHuffmanTree (data, freq, size);
	int array[size], index = 0;
	cout << endl << "The corresponding Huffman encoding is:" << endl;
	PrintCodes (root, array, index);
}

int main (void) {
	int size;
	cout << "Enter the number of characters you want to enter and write the characters along with their frequency:" << endl;
	cin >> size;
	char data[size];
	int freq[size];
	for (int i = 0; i < size; i++) {
		cin >> data[i] >> freq[i];
	}
	HuffmanEncode (data, freq, size);
	return 0;
}
