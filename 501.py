#coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#法一：遍历BST树 利用字典 将数字作为key，次数作为value,然后找出字典中的次数最多的key值 需要额外空间O(n)
class Solution(object):
    numdict={}
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.initNumLst(root)
        maxnum=0
        maxk=-1
        maxlst=[]
        for k in self.numdict:
            if self.numdict[k]>=maxnum:
                if self.numdict[k]>maxnum:
                    maxnum=self.numdict[k]
                    maxlst=[]
                maxlst.append(k)

        return maxlst
        
    def initNumLst(self,root):
        if root==None:
            return
        self.initNumLst(root.left)
        if self.numdict.get(root.val)==None:
            self.numdict[root.val]=1
        else:
            self.numdict[root.val]+=1
        self.initNumLst(root.right)

    
#法二：中序遍历二叉树，得到一个升序序列，遍历时记录前一个值，看当前值的出现频率是否大于前一个值，是则记录
class Solution2(object):
    max=0
    count=0
    maxlst=[]
    pre=None
    def findMode(self, root):
        self.func(root)
        return self.maxlst

    def func(self,root):
        if root==None:
            return
        self.func(root.left)
        if self.pre!=None:
            if root.val==self.pre.val:
                self.count+=1
                if self.count>=self.max:
                    if self.count>self.max:
                        self.maxlst=[]
                        self.max=self.count
                    self.maxlst.append(root.val)
            else:
                self.count=1
            self.pre=root
        else:
            self.pre=root
            self.max=1
            self.count=1
            self.maxlst.append(root.val)
        self.func(root.right)


