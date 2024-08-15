class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')

#Реверсування однозв'язного списку
def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

#Сортування вставками
def insertion_sort_linked_list(linked_list):
    sorted_list = LinkedList()
    current = linked_list.head
    while current:
        next_node = current.next
        insert_into_sorted_list(sorted_list, current)
        current = next_node
    linked_list.head = sorted_list.head

def insert_into_sorted_list(sorted_list, node):
    if not sorted_list.head or sorted_list.head.value >= node.value:
        node.next = sorted_list.head
        sorted_list.head = node
    else:
        current = sorted_list.head
        while current.next and current.next.value < node.value:
            current = current.next
        node.next = current.next
        current.next = node

#Злиття двох списків
def merge_sorted_linked_lists(list1, list2):
    dummy = Node()
    tail = dummy
    
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = merge_sorted_linked_lists(list1.head, list2.head)

current = merged_list.head
while current:
    print(current.value, end=' -> ')
    current = current.next
print('None')
