# Definition for singly-linked list.
class ListNode(object):
 def __init__(self, x):
     self.val = x
     self.next = None

def getListSize(head):
    size = 0
    while head is not None:
        size += 1
        head = head.next;
    return size

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        size = getListSize(head);
        listTocheck = []
        itr = 0

        while itr < size/2:
            listTocheck += [head.val]
            head = head.next
            itr += 1

        if (size%2 == 1):
            itr -= 1

        while itr >0 :
            itr -= 1
            if listTocheck[itr] != head.val:
                return False
            head = head.next

        return True

head = ListNode(1);
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
sol = Solution()
print(sol.isPalindrome(head))