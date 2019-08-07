Each block in blockchain has index, timestamp with current utctime, data as a string, hash
of previous block and this block's hash created by hash of other attributes


Blockchains has an initial block, genesis block, subsequent blocks contain the previous block's hash.
genesis block has index, hash of "0" and arbitary data.

Each block is added at the next index and uses hash of the previous block.
size and to_str methods are implemented.


Time Complexity: Traverse the linked list takes O(n), Insertion/Deletion takes O(1)
Space Complexity: O(n)
