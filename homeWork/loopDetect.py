#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  DESCRIPTION:
#       AUTHOR: artemirk@gmail.com ()
# ===============================================================================

from LinkedList import LinkedList


def loop_detection(ll):
        slow, fast = ll.head, ll.head
        if fast and fast.next:
            fast = fast.next.next
        
        while fast and fast.next and slow is not fast:
            slow, fast = slow.next, fast.next.next

        if fast is None or fast.next is None:
            return None

        slow = ll.head
        fast = fast.next.next
        while fast is not slow:
            fast = fast.next
            slow = slow.next

        return fast


ll = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
cur = sv = ll.head

while cur.next:
    if cur.value == 5:
        sv = cur
    cur = cur.next
cur.next = sv

print(loop_detection(ll))
while cur.next:
    print(cur.value)
    cur = cur.next
