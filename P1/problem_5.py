import hashlib
import datetime

class Block:
    def __init__(self,index,timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    def calc_hash(self):
        sha = hashlib.sha256()
        """
        Hashing is a process which you turn anything (as long as you can represent it as a string) into a fixed 256 bit string. Any input will be turned into output length of random characters string(for bit string output will have 256 characters length , thats why sha-256
        """
        hash_str = "We are going to encode this string of data!".encode('utf-8')

        #sha.update(hash_str)
        sha.update((str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash)).encode('utf-8'))

        return sha.hexdigest()
    # self.hash is usually created by hashing other 4 values
    def get_utc_time(self):
        return datetime.datetime.utcnow()

class Blockchain:
    def __init__(self):
        self.head = None
    def add_block(self):
        if self.head is None:
            self.head = Block(0,datetime.datetime.utcnow(),"genesis_block","0")
            return
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Block(node.index+1,datetime.datetime.utcnow(),"Hey I am Block{}".format(node.index), node.hash)
     
    def size(self):
        size = 0
        node = self.head
        while node:
            size = size + 1
            node = node.next
        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.data)
            node = node.next
        return out

blockchain = Blockchain()
blockchain.add_block()
blockchain.add_block()
blockchain.add_block()
print("Full BlockChain\n")
print(blockchain.to_list())
print("chain head: {}\n".format(blockchain.head.data))

block2 = blockchain.head.next
block3 = blockchain.head.next.next
print("Hash of second block matches previous hash of third block\n")
print(block2.hash == block3.previous_hash)

#output
"""
Full BlockChain

['genesis_block', 'Hey I am Block0', 'Hey I am Block1']
chain head: genesis_block

Hash of second block matches previous hash of third block

True
"""
