# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy head of the result linked list
        current = dummy_head  # Current node for traversal
        carry = 0  # Carry value for addition

        while l1 or l2 or carry:
            # Calculate the sum of the current digits and carry
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            # Update carry and create a new node with the sum digit
            carry = sum_val // 10
            digit = sum_val % 10
            current.next = ListNode(digit)

            # Move to the next nodes
            current = current.next

        return dummy_head.next  # Return the result linked list without the dummy head