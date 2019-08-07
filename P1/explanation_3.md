Huffman coding assigns codes to input characters in the given text,
based on the frequencies of character occurence.Most frequent character
gets the smallest length code and vice versa.

First step was to build the dictionary of each character and its frequency.
Then a min-heap is built,as a tree structure. Leaf nodes are characters with minimum frequency and non-leaf
nodes are created from merging leaf nodes, repeatedly.

each node of tree had attributes char,frquency,left and right pointer
and overloaded less than operator to compare frequencies. Also an encode
function to return bit coding in traversal.

heapq modules' heapify method is used to create the min heap.
After the tree is built, it is traversed recursively and each char
in nodes are assigned corresponding codes.Thus a dictionary is built of char and its code.
Then all the codes are concated together.

Greedy top-down approach of building the tree creates n sub-tree for n characters.For each subtree,
it combines the two least frequency leaf nodes as frequency of the root and so on.
If heap is used, to find cheapest weight and insertion takes 0(logn)in worst case. 
For each character of n, there are 0(n) iterations, thus total complexity is 0(nlogn).

For decode, we iterate through tree by starting from root.
If current bit is 0, left node otherwise right node is selected.
When we reach leaf, print the character of that node and start from root again.


Time complexity : O(nlogn)
Space complexity : O(n)

