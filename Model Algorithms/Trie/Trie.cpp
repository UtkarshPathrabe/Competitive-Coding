#include <bits/stdc++.h>
#define	ALPHABET_SIZE	26
#define	ARRAY_SIZE(a)	(sizeof(a) / sizeof(a[0]))
#define	CHAR_TO_INDEX(c)	((int)c - (int)'a')

using namespace std;

typedef	struct node	trieNode;
struct node {
	int value;
	trieNode *children[ALPHABET_SIZE];
};

typedef struct t trie;
struct t {
	trieNode *root;
	int count;
};

trieNode *getNode () {
	trieNode *pNode = (trieNode*) malloc (sizeof(trieNode));
	if (pNode) {
		pNode->value = 0;
		for (int i = 0; i < ALPHABET_SIZE; i++) {
			pNode->children[i] = NULL;
		}
	}
	return pNode;
}

void initialize (trie *pTrie) {
	pTrie->root = getNode();
	pTrie->count = 0;
}

void insertKey (trie *pTrie, char key[]) {
	trieNode *pNode = pTrie->root;
	pTrie->count++;
	for (int level = 0; level < strlen(key); level++) {
		int index = CHAR_TO_INDEX(key[level]);
		if (pNode->children[index] == NULL) {
			pNode->children[index] = getNode();
		}
		pNode = pNode->children[index];
	}
	pNode->value = pTrie->count;
}

int searchKey (trie *pTrie, char key[]) {
	trieNode *pNode = pTrie->root;
	for (int level = 0; level < strlen(key); level++) {
		int index = CHAR_TO_INDEX(key[level]);
		if (pNode->children[index] == NULL) {
			return 0;
		}
		pNode = pNode->children[index];
	}
	return (pNode != NULL && pNode->value);
}

bool isLeafNode (trieNode *pNode) {
	return (pNode->value != 0);
}

bool isFreeNode (trieNode *pNode) {
	for (int i = 0; i < ALPHABET_SIZE; i++) {
		if (pNode->children[i]) {
			return false;
		}
	}
	return true;
}

bool deleteHelper (trieNode *pNode, char key[], int level, int len) {
	if (pNode) {
		if (level == len) {
			if (pNode->value) {
				pNode->value = 0;
				return isFreeNode(pNode);
			}
		} else {
			int index = CHAR_TO_INDEX(key[level]);
			if (deleteHelper(pNode->children[index], key, level + 1, len)) {
				free(pNode->children[index]);
				pNode->children[index] = NULL;
				return ((!isLeafNode(pNode)) && (isFreeNode(pNode)));
			}
		}
	}
	return false;
}

void deleteKey (trie *t, char key[]) {
	if (strlen(key) > 0) {
		deleteHelper (t->root, key, 0, strlen(key));
	}
}

int main (void) {
	char keys[][8] = {"the", "a", "there", "answer", "any", "by", "bye", "their", "she", "sells", "sea", "shore", "sheer"};
	char output[][32] = {"Not Present in Trie.\n", "Present in Trie.\n"};
	trie t;
	initialize(&t);
	for (int i = 0; i < ARRAY_SIZE(keys); i++) {
		insertKey(&t, keys[i]);
	}
	printf("the --- %s", output[searchKey(&t, (char *)"the")]);
	printf("these --- %s", output[searchKey(&t, (char *)"these")]);
	printf("their --- %s", output[searchKey(&t, (char *)"their")]);
	printf("thaw --- %s", output[searchKey(&t, (char *)"thaw")]);
	printf("by --- %s", output[searchKey(&t, (char *)"by")]);
	deleteKey (&t, keys[0]);
	deleteKey (&t, keys[6]);
	cout << "After deleteing..." << endl;
	printf("the --- %s", output[searchKey(&t, (char *)"the")]);
	printf("by --- %s", output[searchKey(&t, (char *)"by")]);
	printf("bye --- %s", output[searchKey(&t, (char *)"bye")]);
	return 0;
}
