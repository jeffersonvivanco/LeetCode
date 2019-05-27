class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    l1_temp = l1
    l2_temp = l2

    res = None
    res_temp = None

    carry_over = 0

    while l1_temp != None or l2_temp != None:

        total = carry_over
        if l1_temp != None:
            total += l1_temp.val
            l1_temp = l1_temp.next

        if l2_temp != None:
            total += l2_temp.val
            l2_temp = l2_temp.next

        carry_over = 0
        if total >= 10:
            total = total % 10
            carry_over = 1

        if res_temp == None:
            res_temp = ListNode(total)
            res= res_temp
        else:
            res_temp.next = ListNode(total)
            res_temp = res_temp.next

    if carry_over == 1:
        res_temp.next = ListNode(carry_over)

    return res

import unittest

class AddTwoNumbersTest(unittest.TestCase):

    def test_add_two_numbers(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        res = addTwoNumbers(l1, l2)

        while res != None:
            print(res.val)
            res = res.next

unittest.main()