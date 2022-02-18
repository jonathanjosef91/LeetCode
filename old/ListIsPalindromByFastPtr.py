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
        listTocheck = []
        fastPtr = head

        while fastPtr is not None and fastPtr.next is not None:
            fastPtr = fastPtr.next.next
            listTocheck.append(head.val)
            head = head.next

        if (fastPtr is not None):
            head = head.next

        while head:
            if listTocheck.pop() != head.val:
                return False
            head = head.next

        return True

head = ListNode(1);
head.next = ListNode(2)
head.next.next = ListNode(2)
#head.next.next.next = ListNode(2)
#head.next.next.next.next = ListNode(1)
sol = Solution()
print(sol.isPalindrome(head))