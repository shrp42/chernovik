# < 5. Связанные списки >

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# * Reverse Linked List.
def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_linked_list_recursive(head)
cur = reversed_head
while cur:
    print(cur.val, end=" → ")
    cur = cur.next
print("None")


# ----------------------------------------------------------------------


# * Merge Two Sorted Lists.
def merge_two_sorted_lists_recursive(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val < l2.val:
        l1.next = merge_two_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_lists_recursive(l1, l2.next)
        return l2


l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged = merge_two_sorted_lists_recursive(l1, l2)
cur = merged
while cur:
    print(cur.val, end=" → ")
    cur = cur.next
print("None")


# ----------------------------------------------------------------------


# * Linked List Cycle Detection.
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 1 → 2 → 3 → 4 → 2 (цикл)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # создаём цикл
print(has_cycle(node1))  # True

# 1 → 2 → 3 → 4 → None (без цикла)
node4.next = None
print(has_cycle(node1))  # False


# ----------------------------------------------------------------------


# * Remove Nth Node From End.
def remove_nth_from_end_recursive(head, n):
    def helper(node):
        if not node:
            return 0, node
        pos, node.next = helper(node.next)
        pos += 1
        if pos == n:
            return pos, node.next  # пропускаем этот узел
        return pos, node

    _, new_head = helper(head)
    return new_head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = remove_nth_from_end_recursive(head, 2)
cur = new_head
while cur:
    print(cur.val, end=" → ")
    cur = cur.next
print("None")

