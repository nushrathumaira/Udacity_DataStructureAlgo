LRU_cache holds all nodes in hash map which has insertion and search in constant, 0(1) time.
Hash map stores the page numbers as key and address of the node of queue structure , which is the lru cache itself.
Queue is a double linked list thus each node has previous and next pointer. 
front of queue has most recent pages and end has least recent ones.

get method search a page in cache and if it is there removes the node from where it was and bring it to front of queue.
set method is called to set the key for the page if it is not in cache.
set adds a new node to front and update the hash map.
Both get and set takes O(1) time. Space complexity would be the order of number of elements.

time complexity for insertion/search : 0(1)
space complexity : O(n)