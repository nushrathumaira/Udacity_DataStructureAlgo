class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        cur_head = self.head
        if cur_head is None:
            return ""
        out_string = ""
        while cur_head.next is not None:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += str(cur_head.value)
        return out_string
     
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    def replicate(self):
        copy = LinkedList()
        current = self.head
        while current:
            copy.append(current.value)
            current = current.next
        return copy


        
    def remove(self,node):
        current = self.head
        while( current and current.next != node):
            current = current.next
        prev_node = current
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

def deduplicate(llist):
    current1 = llist.head
    while current1:
        current2 = current1.next
        value = current1.value
        while current2:
            temp = current2
            current2 = current2.next
            if temp.value == value:
                llist.remove(temp)
        current1 = current1.next

def union(llist_1,llist_2):
    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1
    result = llist_1.replicate()
    last = result.head
    
    while last.next is not None:
        last = last.next
    llist_2_copy = llist_2.replicate()
    last.next = llist_2_copy.head
    
    deduplicate(result)

    return result
    
def intersection(llist_1, llist_2):
    if (llist_1 is None or llist_2.head is None):
        return None
    result = LinkedList()
    current1 = llist_1.head
    while current1:
        current2 = llist_2.head
        value = current1.value
        while current2:
            if current2.value == value:
                result.append(value)
                break
            current2 = current2.next
        current1 = current1.next
    deduplicate(result)

    return result



# Test case 1
print("Test case 1\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


test1_union_result = union(linked_list_1,linked_list_2)
test1_union_answer = "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11"
print ("Pass" if (str(test1_union_result) == test1_union_answer) else "Fail")
test1_intersection_result=intersection(linked_list_1,linked_list_2)
test1_intersection_answer = "4 -> 6 -> 21"
print ("Pass" if (str(test1_intersection_result) == test1_intersection_answer) else "Fail")
# Test case 2
print("Test case 2")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

test2_union_result = union(linked_list_3,linked_list_4)
test2_union_answer = "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21"
print ("Pass" if (str(test2_union_result) == test2_union_answer) else "Fail")
test2_intersection_result=intersection(linked_list_3,linked_list_4)
test2_intersection_answer = ""
print ("Pass" if (str(test2_intersection_result) == test2_intersection_answer) else "Fail")
print("Test case 3\n")
linked_list5 = LinkedList()
linked_list6 = LinkedList()


element_1 = [None,2,2,None]

element_2 = [1,2,3,5,7,9]


for i in element_1:

    linked_list5.append(i)


for i in element_2:

    linked_list6.append(i)



test5_union_result = union(linked_list5, linked_list6)

test5_union_answer = "None -> 2 -> 1 -> 3 -> 5 -> 7 -> 9"

test5_intersection_result = intersection(linked_list5, linked_list6)

print ("Pass" if (str(test5_union_result) == test5_union_answer) else "Fail")

print ("Pass" if (str(test5_intersection_result) == "2") else "Fail")
