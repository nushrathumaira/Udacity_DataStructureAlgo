import sys
import heapq

class Node:
    def __init__(self,freq, char = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self,other):
        if(other == None):
            return -1
        if(not isinstance(other,Node)):
            return -1
        return self.freq < other.freq
    def encode(self,encoding):
        """ return bit encoding in traversal """
        if self.left is None and self.right is None:
            yield (self.char, encoding)
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v

def pad_encoded_text(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"

    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text
    return encoded_text
def remove_padding(padded_encoded_text):
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info,2)

    padded_encoded_text = padded_encoded_text[8:]
    encoded_text = padded_encoded_text[:-1*extra_padding]

    return encoded_text
def huffman_encoding(data):
    freq_dict = {}
    min_heap = []
    tree = {}

    for char in data:
        freq_dict[char] = freq_dict.get(char,0) + 1
    """
    for key in freq_dict:
        node = Node(key, freq_dict[key])
        heapq.heappush(min_heap, node)
    """
    priority_queue = []
    for key in freq_dict:
        priority_queue.append(Node(freq_dict[key],key))
    heapq.heapify(priority_queue)
    # if only character to encode
    """
    if len(priority_queue) == 1:
        root = Node(1)
        root.left = priority_queue[0]
    """
    while len(priority_queue) > 1 :
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged = Node(node1.freq+node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(priority_queue, merged)
    """    
    while(len(min_heap) > 1 ):# as long as there is one node in heap
        node1 = heapq.heappop(min_heap) # pops off smalles element
        node2 = heapq.heappop(min_heap)

        merged = Node(None, node1.freq+ node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(min_heap,merged)
     """
    root = priority_queue[0]
    encoding = {}
    for char, code in priority_queue[0].encode(''):
        encoding[char] = code
     
    bits = ''
    for _ in data:
        if not _ in encoding:
            raise ValueError("'"+ _ + "' is not encoded character")
        bits += encoding[_]
    return bits, root

def huffman_decoding(data,tree):
    """
    decoded = []
    i = 0
    while i < len(data):
        ch = data[i]
        act = tree[ch]
        while not isinstance(act,str):
            i += 1
            ch = data[i]
            act = act[ch]
        decoded.append(act)
        i += 1
    return decoded
    """
    node = tree
    s = ''
    for _ in data:
        if _ == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            s += node.char
            node = tree
    return s
if __name__ == "__main__":
    codes = {}
    print("First test case\n")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    padded_encoded_data = pad_encoded_text(encoded_data)
    print("The content of padded encoded data is: {}\n".format(padded_encoded_data))
    encoded_text = remove_padding(padded_encoded_data)
    decoded_data = huffman_decoding(encoded_text, tree)
    #decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    print("Second test case\n")
    second_sentence = "Quick brown fox jumps over the lazy dog"
    print ("The size of the data is: {}\n".format(sys.getsizeof(second_sentence)))
    print ("The content of the data is: {}\n".format(second_sentence))
    
    encoded_data, tree = huffman_encoding(second_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    padded_encoded_data = pad_encoded_text(encoded_data)
    print("The content of padded encoded data is: {}\n".format(padded_encoded_data))
    encoded_text = remove_padding(padded_encoded_data)
    decoded_data = huffman_decoding(encoded_text, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # output
    """
    First test case
    
    The size of the data is: 69
    
    The content of the data is: The bird is the word
    
    The size of the encoded data is: 36
    
    The content of the encoded data is: 1110111111101010001100110000101100101101101011111101010000111001100001
    
    The content of padded encoded data is: 00000010111011111110101000110011000010110010110110101111110101000011100110000100
    
    The size of the decoded data is: 69
    
    The content of the encoded data is: The bird is the word
    
    Second test case
    
    The size of the data is: 88
    
    The content of the data is: Quick brown fox jumps over the lazy dog
    
    The size of the encoded data is: 48
    
    The content of the encoded data is: 1001100101001011101100010110100011011010000110000111011111001001100110111100001010000011110111011001011101011100101111010101101001110011000111000000110100110110111101010111111
    
    The content of padded encoded data is: 0000000110011001010010111011000101101000110110100001100001110111110010011001101111000010100000111101110110010111010111001011110101011010011100110001110000001101001101101111010101111110
    
    The size of the decoded data is: 88
    
    The content of the encoded data is: Quick brown fox jumps over the lazy dog
    """