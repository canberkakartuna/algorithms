/*
 * Binary Search Tree:
 *  1. At most 2 children
 *  2. Left subtree is always smaller than root
 *  3. Right subtree is always larger than root
 */

class Node {
	constructor(data, left = null, right = null) {
		this.data = data;
		this.left = left;
		this.right = right;
	}
}

class BST {
	constructor() {
		this.root = null;
	}

	insert(data) {
		const node = new Node(data);

		if (this.root) {
			function insertNode(treeNode, newNode) {
				if (newNode.data > treeNode.data) {
					if (!treeNode.right) {
						treeNode.right = newNode;
					} else {
						treeNode = treeNode.right;
						insertNode(treeNode, node);
					}
				} else {
					if (!treeNode.left) {
						treeNode.left = newNode;
					} else {
						treeNode = treeNode.left;
						insertNode(treeNode, node);
					}
				}
			}

			insertNode(this.root, node);
		} else {
			this.root = node;
		}
	}

	find(data) {
		function findNode(node, data) {
			if (data == node.data) {
				return node;
			} else if (data > node.data) {
				if (node.right) {
					node = node.right;
					return findNode(node, data);
				} else return -1;
			} else if (data < node.data) {
				if (node.left) {
					node = node.left;
					return findNode(node, data);
				} else return -1;
			}
		}
		return findNode(this.root, data);
	}

	/**
	 * TODO:
	 * findMinNode()
	 * getRootNode()
	 * inorder(node)
	 * preorder(node)
	 * postorder(node)
	 * search(node, data)
	 */

	getTree() {
		return this.root;
	}
}

const tree = new BST();

tree.insert(10);
tree.insert(7);
tree.insert(15);
tree.insert(12);
tree.insert(3);
tree.insert(7);
tree.insert(25);

console.log(tree.find(117));
