class QNode(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        return "(%s, %s)" % (self.key,self.value)

class LRU_Cache(object):
    def __init__(self,capacity):
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")
        self.hash_map = {}

        self.head = None
        self.end = None
        self.capacity = capacity
        self.current_size = 0
    def get(self,key):
        # get the value(will always be positiive) if the key exists in cache, otherwise return -1

        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        # return value if we are already at head
        if self.head == node:
            return node.value
        self.remove(node)
        self.set_head(node)
        return node.value
    def set(self,key,value):
        # set the value if key is not present in cache
        #
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value

            #update pointers ( correspoding node address ?) only if this is not head, otherwise return
            if self.head != node:
                self.remove(node)
                self.set_head(node) # bring the node to front of queue, to bring in memory
                # and also update node address in hash
        else:
            new_node = QNode(key,value)
            if self.current_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.set_head(new_node)
            self.hash_map[key] = new_node # bring new node to front and update node_address in hash
    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.current_size += 1
    def remove(self,node):
        if not self.head:
            return
           # remove node from middle, update pointers
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
           # head = end = node
        if not node.next and node.prev:
            self.head = None
            self.end = None
           # if the node we are removing is the one at the end, update the new end
           # set new end previous to be null
        if self.end == node:
            self.end = node.next
            self.end.prev = None
        self.current_size -= 1
        return node
    def print_elements(self):
        n = self.head
        print("[head = %s, end = %s]" % (self.head, self.end), end=" ")
        while n:
            print("%s -> " % (n), end = "")
            n = n.prev
        print("NULL")

our_cache = LRU_Cache(5)

our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(2,3)
our_cache.set(1,5)
our_cache.set(4,5)
our_cache.set(6,7)
#our_cache.print_elements()
print(our_cache.get(1)) # returns 5
print(our_cache.get(2))  # returns  3
print(our_cache.get(3)) # returns -1
print(our_cache.get(4)) #returns 5
print(our_cache.get(5)) #returns -1
print(our_cache.get(6)) #returns 7


