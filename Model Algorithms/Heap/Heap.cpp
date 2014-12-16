/* Author: Utkarsh Pathrabe */

#include <bits/stdc++.h>

using namespace std;

int HEAPSIZE = 0;
vector<int> HEAP;

int PARENT(int i) {
	return (ceil(i/2.0) - 1);
}

int LEFT(int i) {
	return ((2*i) + 1);
}

int RIGHT(int i) {
	return ((2*i) + 2);
}

void SWAP(int *i, int *j) {
	int temp = *i;
	*i = *j; 
	*j = temp;
}

int LENGTH(vector<int> &A) {
	return A.size();
}

void PRINT_HEAP(vector<int> &A) {
	printf("The present HEAP contents are:\n");
	for(vector<int>::iterator it = A.begin(); it != A.end(); it++){
		printf("%d\t", *it);
	}
	printf("\n");
}

/* MAX-HEAPIFY is an important subroutine for manipulating max-heaps. Its inputs are an array A and an index i into the array. When MAX-HEAPIFY is called, it is assumed that the
binary trees rooted at LEFT(i) and RIGHT(i) are max-heaps, but that A[i] may be smaller than its children, thus violating the max-heap property. The function of MAX-HEAPIFY is to let
the value at A[i] "float down" in the max-heap so that the subtree rooted at index i becomes a max-heap. */
void MAX_HEAPIFY(vector<int> &A, int i) {							// Each call costs O(lg(n)) time
	int left = LEFT(i);
	int right = RIGHT(i);
	int largest;
	if((left <= (HEAPSIZE - 1)) && (A[left] > A[i])){
		largest = left;
	}else{
		largest = i;
	}
	if((right <= (HEAPSIZE - 1)) && (A[right] > A[largest])){
		largest = right;
	}
	if(largest != i){
		SWAP(&A[i], &A[largest]);
		MAX_HEAPIFY(A, largest);
	}
}

/* The procedure MAX-HEAPIFY converts an array A[1,...,n-1], where n = length[A] in a bottom-up manner into a max-heap. */
void BUILD_MAX_HEAP(vector<int> &A) {								// Running time is O(n lg(n)) because each call to MAX-HEAPIFY costs O(lg(n)) time, and there are O(n) such calls 
																	// but it is not asymptotically tight. The tighter bound is O(n).
	for (int i = floor((HEAPSIZE - 1) / 2); i >= 0; i--){
		MAX_HEAPIFY(A, i);
	}
}

/* The heapsort algorithm starts by using BUILD-MAX-HEAP to build a max-heap on the input array A[0,...,n-1], where n = LENGTH(A). Since the maximum element of the array is stored at the
root A[0], it can be put into its correct final position by exchanging it with A[n-1]. If we now "discard" node n-1 from the heap (by decrementing heap-size), we observe that A[1,...,(n-2)] 
can easily be made into a max-heap. The children of the root remain max-heaps, but the new root element may violate the max-heap property. All that is needed to restore the maxheap
property, however, is one call to MAX-HEAPIFY(A, 0), which leaves a max-heap in A[1,...,(n-2)]. The heapsort algorithm then repeats this process for the max-heap of size n-1
down to a heap of size 1. */
void HEAP_SORT(vector<int> &A) {									// The HEAPSORT procedure takes time O(n lg(n)), since the call to BUILD-MAX-HEAP takes time O(n) and each of
	printf("After running heapsort:\n");							// the n - 1 calls to MAX-HEAPIFY takes time O(lg(n)).
	BUILD_MAX_HEAP(A);
	for (int i = HEAPSIZE - 1; i > 0; i--) {
		SWAP(&A[0], &A[i]);
		HEAPSIZE -= 1;
		MAX_HEAPIFY(A, 0);
	}
	HEAPSIZE = LENGTH(A);
}

/* The procedure ADD_ELEMENT adds the new element 'key' to the heap */
void ADD_ELEMENT(vector<int> &A, int key) {							// It takes O(1) time
	A.push_back(key);
	HEAPSIZE = LENGTH(A);
}

/* The procedure REMOVE-ELEMENT removes the element at given index from the heap */
void REMOVE_ELEMENT(vector<int> &A, int index) {					// It takes O(n) time
	if(index >= LENGTH(A) || index < 0) {
		printf("\t*****ERROR!!!*****\nThe given index %d does not exist in the heap.\n", index);
	}else{
		A.erase(A.begin() + index);
	}
	HEAPSIZE = LENGTH(A);
}

/* The procedure HEAP-MAXIMUM implements the MAXIMUM operation */
int HEAP_MAXIMUM(vector<int> &A) {									// It takes O(lg(n)) time because we are calling MAX_HEAPIFY otherwise, it takes O(1) time, if we don't call MAX_HEAPIFY.
	MAX_HEAPIFY(A, 0);
	return A[0];
}

/* The procedure HEAP-EXTRACT-MAX implements the EXTRACT-MAX operation. */
int HEAP_EXTRACT_MAXIMUM(vector<int> &A) {							// It takes O(lg(n)) time but it will take O(n) time because of erase() function.
	if(HEAPSIZE < 0) {
		printf("\t*****ERROR!!!*****\nHeap Underflow!");
	}
	int max = HEAP_MAXIMUM(A);
	A[0] = A[HEAPSIZE - 1];
	A.pop_back();
	MAX_HEAPIFY(A, 0);
	//A.erase(A.begin());
	HEAPSIZE = LENGTH(A);
	return max;
}

/* The procedure HEAP-INCREASE-KEY implements the INCREASE-KEY operation. The priority-queue element whose key is to be increased is identified by an index i into the array.
The procedure first updates the key of element A[i] to its new value. Because increasing the key of A[i] may violate the max-heap property, the procedure then, traverses a path from
this node toward the root to find a proper place for the newly increased key. During this traversal, it repeatedly compares an element to its parent, exchanging their keys and
continuing if the element's key is larger, and terminating if the element's key is smaller, since the max-heap property now holds. */
void HEAP_INCREASE_KEY(vector<int> &A, int i, int key) {			// Its Running time is O(lg(n))
	if(key < A[i]) {
		printf("\t*****ERROR!!!*****\nNew key is smaller than the older key.");
	}
	A[i] = key;
	while(i > 0 && A[i] > A[PARENT(i)]) {
		SWAP(&A[i], &A[PARENT(i)]);
		i = PARENT(i);
	}
}

/* The procedure MAX-HEAP-INSERT implements the INSERT operation. It takes as an input the key of the new element to be inserted into max-heap A. The procedure first expands the
max-heap by adding to the tree a new leaf whose key is minInt. Then it calls HEAP-INCREASEKEY to set the key of this new node to its correct value and maintain the max-heap property. */
void MAX_HEAP_INSERT(vector<int> &A, int key) {
	ADD_ELEMENT(A, INT_MIN);
	HEAP_INCREASE_KEY(A, HEAPSIZE - 1, key);
}

int main(void){
	ADD_ELEMENT(HEAP, 4);
	ADD_ELEMENT(HEAP, 1);
	ADD_ELEMENT(HEAP, 3);
	ADD_ELEMENT(HEAP, 2);
	ADD_ELEMENT(HEAP, 16);
	ADD_ELEMENT(HEAP, 9);
	ADD_ELEMENT(HEAP, 10);
	ADD_ELEMENT(HEAP, 14);
	ADD_ELEMENT(HEAP, 8);
	ADD_ELEMENT(HEAP, 7);
	PRINT_HEAP(HEAP);
	HEAPSIZE = LENGTH(HEAP);
	BUILD_MAX_HEAP(HEAP);
	PRINT_HEAP(HEAP);
	ADD_ELEMENT(HEAP, 11);
	PRINT_HEAP(HEAP);
	REMOVE_ELEMENT(HEAP, 11);
	REMOVE_ELEMENT(HEAP, -1);
	REMOVE_ELEMENT(HEAP, 3);
	PRINT_HEAP(HEAP);
	printf("The maximum element of heap is:\t%d\n", HEAP_EXTRACT_MAXIMUM(HEAP));
	PRINT_HEAP(HEAP);
	HEAP_INCREASE_KEY(HEAP, 3, 20);
	PRINT_HEAP(HEAP);
	HEAP_SORT(HEAP);
	PRINT_HEAP(HEAP);
	return 0;
}
