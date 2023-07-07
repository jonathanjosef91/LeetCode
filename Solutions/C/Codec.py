import json
import unittest
from queue import Queue
from typing import Optional

from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None



class Solution:
    def getTags(self):
        tags = [Difficulty.Hard, Topic.Design]
        return tags

    # Less efficient solution, but shows a nice concept
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None"

        return f"{str(root.val)}:({self.serialize(root.left)})({self.serialize(root.right)})"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None

        eov_index = data.index(':')
        root = TreeNode(int(data[0:eov_index]))

        data = data[eov_index+1:]
        counter = 1
        eol = 0
        while counter > 0:
            eol += 1
            if data[eol] == "(":
                counter += 1
            if data[eol] == ")":
                counter -= 1

        eor = eol + 1
        counter = 1
        while counter > 0:
            eor += 1
            if data[eor] == "(":
                counter += 1
            if data[eor] == ")":
                counter -= 1

        root.left = self.deserialize(data[1:eol])
        root.right = self.deserialize(data[eol+2:eor])

        return root

    def serialize_a(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            v = q.get()
            if not v:
                res.append(None)
            else:
                res.append(v.val)
                q.put(v.left)
                q.put(v.right)

        return json.dumps(res)

    def deserialize_a(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_list = json.loads(data)

        if data_list[0] is None:
            return None

        lower_level = Queue()
        root = TreeNode(data_list[0])
        lower_level.put(root)
        v_index = 1

        while not lower_level.empty():
            parent: Optional[TreeNode] = lower_level.get()
            if parent is None:
                continue

            next_val = data_list[v_index]
            v_index += 1
            if next_val is not None:
                parent.left = TreeNode(next_val)
                lower_level.put(parent.left)

            next_val = data_list[v_index]
            v_index += 1
            if next_val is not None:
                parent.right = TreeNode(next_val)
                lower_level.put(parent.right)

        return root

class test_Codec(unittest.TestCase):
    def test_1(self):
        root = TreeNode(1)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        data = Solution().serialize(root)
        recovered_root = Solution().deserialize(data)

        print("Done")
