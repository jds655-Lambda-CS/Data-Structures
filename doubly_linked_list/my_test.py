from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

node = ListNode(1)
dll = DoublyLinkedList(node)

print(f'Initial list: {dll}')

dll.add_to_head(40)
#print(f'dll.tail.value, 1')
#print(f'dll.head.value, 40')
print(f'After Adding 40 to head:\n{dll}')

dll.move_to_end(dll.head)
# print(f'{dll.tail.value,} 40')
# print(f'{dll.tail.prev.value}, 1')
print(f'After moving 40 to tail:\n{dll}')
print(f'Length: {len(dll)}, 2')

dll.add_to_tail(4)
print(f'After adding 4 to tail:\n{dll}')
dll.move_to_end(dll.head.next)
# print(f'{dll.tail.value}, 40')
# print(f'{dll.tail.prev.value}, 4')
print(f'After moving head.next® to tail:\n{dll}')
print(f'Length is: {len(dll)}, 3')

