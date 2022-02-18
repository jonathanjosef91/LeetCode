class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = ""
        if not root:
            return data

        data += str(self.__preOrder(root))
        data += "\n"
        data += str(self.__inOrder(root))
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None


        preorderStr, inorderStr = data.split("\n")
        preorder = preorderStr[1:-1].split(",")
        inorder = inorderStr[1:-1].split(",")

        for i in range(len(preorder)):
            preorder[i] = int(preorder[i])
            inorder[i] = int(inorder[i])

        return self.__buildTree(preorder, inorder)

    def __inOrder(self, root):
        if not root:
            return []
        return self.__inOrder(root.left) + [root.val] + self.__inOrder(root.right)

    def __preOrder(self, root):
        if not root:
            return []
        return [root.val] + self.__preOrder(root.left) + self.__preOrder(root.right)


    def __buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        return self.__buildTreeAux(preorder,inorder,0,len(preorder),0,len(inorder))

    def __buildTreeAux(self,preorder,inorder,preS,preE,inS,inE):
        if preS >= preE:
            return None
        root = TreeNode(preorder[preS])
        leftInS , leftInE = inS , inorder.index(root.val)
        rightInS , rightInE = inorder.index(root.val)+1, inE
        leftPreS, leftPreE = preS+1, preS+leftInE-leftInS+1
        rightPreS, rightPreE = preS+leftInE-leftInS+1, preE

        root.left = self.__buildTreeAux(preorder, inorder, leftPreS, leftPreE, leftInS, leftInE)
        root.right = self.__buildTreeAux(preorder, inorder, rightPreS, rightPreE, rightInS, rightInE)

        return root
