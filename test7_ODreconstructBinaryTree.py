# -*- coding:utf-8 -*-
"""
File: reconstructBinaryTree.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle
Description:
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = TreeNode(new_node)
        else:
            t = TreeNode(new_node)
            t.left = self.left
            self.left = t.left

    def insert_right(self, new_node):
        if self.right is None:
            self.right = TreeNode(new_node)
        else:
            t = TreeNode(new_node)
            t.right = self.right
            self.right = t.right

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_val(self, obj):
        self.val = obj

    def get_root_val(self):
        return self.val


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        """ 重建二叉树

        根据前序的第一个值是根节点的特点，查找中序的对应值，拆成左右子树，分别对左右子树进行如上递归操作

        Args:
            pre (list): preorder values list
            tin (list): inorder values list

        Returns:
            返回构造的TreeNode根节点
        """
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        idx = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:idx + 1], tin[0:idx])
        root.right = self.reConstructBinaryTree(pre[idx + 1:], tin[idx + 1:])

        return root


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def print_tree(tree):
    if tree:
        print(" (", end="")
        print(tree.val, end="")
        print_tree(tree.left)
        print_tree(tree.right)
        print(") ", end="")
    else:
        print("()", end="")


if __name__ == "__main__":
    s = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    root = s.reConstructBinaryTree(pre, tin)
    print("==========Preorder")
    preorder(root)
    print("==========Inorder")
    inorder(root)
    print("==========Postorder")
    postorder(root)
    print("==========Tree")
    print_tree(root)
