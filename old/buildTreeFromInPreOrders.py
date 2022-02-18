# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        return self.__buildTree(preorder,inorder,0,len(preorder),0,len(inorder))

    def __buildTree(self,preorder,inorder,preS,preE,inS,inE):
        if preS >= preE:
            return None
        root = TreeNode(preorder[preS])
        leftInS , leftInE = inS , inorder.index(root.val)
        rightInS , rightInE = inorder.index(root.val)+1, inE
        leftPreS, leftPreE = preS+1, preS+leftInE-leftInS+1
        rightPreS, rightPreE = preS+leftInE-leftInS+1, preE

        root.left = self.__buildTree(preorder, inorder, leftPreS, leftPreE, leftInS, leftInE)
        root.right = self.__buildTree(preorder, inorder, rightPreS, rightPreE, rightInS, rightInE)

        return root


sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(sol.buildTree(preorder,inorder))