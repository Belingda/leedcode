# coding=utf-8
# 寻找两个节点的最近公共节点

# 法一：递归 时间复杂度o(n)（通用树）
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        leftnode = self.lowestCommonAncestor(root.left, p, q)
        rightnode = self.lowestCommonAncestor(root.right, p, q)
        if leftnode == None:
            print(rightnode.val)
            return rightnode
        elif rightnode == None:
            print(leftnode.val)
            return leftnode

        return root

# 法二 针对bst树特点
    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node=root
        while node:
            if p.val<node.val and q.val<node.val:
                node=node.left
            elif p.val>node.val and q.val>node.val:
                node=node.right
            else:
                return node
                
