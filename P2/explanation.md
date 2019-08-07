#problem 1

square root of an integer exist in the range between 0 and that integer.
while we are within this range, we choose a number at the middle of range.
if mid squared equals the given number, then mid is the root.
if x is smaller than mid squared, then binary search between start and mid.
otherwise binary search mid+1 and end. 

Time Complexity : O(logn) as binary search
Space Complexity: O(1) as the iterative binary search is implemented

#problem 2

First a pivot point needs to be selected, based around pivot divide the input array to 
two sub arrays. Pivot element is the one whose next element in the sorted array is smaller than it.
If number to search is greater than the zeroth element, search in left sub array
otherwise right sub array. Recursion is used in both finding pivot and binary search of the element

Time Complexity: O(logn) as every time we only search in one half and discard the other half.
Space Complexity: O(1) and O(logn) auxilliary space for call stack space created by recursive binary search call.


#problem 3

First the given array is sorted using count sort in descending order. 
I chose counting sort as it offers time complexity O(n+k) where n values in the
array ranges from 0 to k. So for smaller range, it works faster merge sort or quicksort.
Then to form the two numbers to get maximum sum, we get alternating digits,
one number contains array digits at odd indices and other one with digits at
even indices.

Time Complexity: O(n+k)
Space Complexity: O(n+k) for input array of size n and count array of size k

#problem 4

Sorting the numbers by counts of 0,1,2 and putting them in the array would require
O(n) and traverse the array twice. Instead my solution uses 1 as the pivot value and divides
the array into groups with values less than, equal to and greater than the pivot.

Time Complexity: O(n)
Space Complexity: O(1)

#problem 5

Insert and find in Trie is from the classroom practice we did before. Trie Nodes are initialized with a flag
is_word and a dictionary for children. recursive suffix function uses a generator to iterate over the trie
according to suffix. Once the node at the end of suffix is reached, recursively the sub-trie is iterated while keeping suffix in track
and yield when terminal node is found or is_word becomes true.

Now we call find function to find the prefix and then suffixes to generate all suffixes of the given prefix.

Time Complexity:
There are two functions to consider, insert() and suffixes(). Insertion in a trie depends on how many words in the trie and the length of those words.
Worst case time complexity for creation of trie is O(nm) where n is number of words and m length of longest word.Finding suffixes would also take O(na) where n is number of words and a is length of word we are searching for suffixes.
It takes O(n) to traverse all nodes in Trie.
Space Complexity: 
Creation of trie takes up quite a lot of space. Inserting a new word/node doesn't add much extra space as several branches are already built up.
If the returned suffixes were a list filled up with all words then space complexity would be O(nm) same as time complexity.
By using a generator it would generate the suffixes on the fly and no need to store them in a list so that would save a lot of auxilliary space.


#problem 6

The array is divided into two parts, the maximum and minimum of two parts are compared recursively.
The max,min from two parts are found by two recursive call of the get_min_max_recursive function.
Then one comparison to find max of two maxes of two parts and same goes for minimum.

Time Complexity : O(n)
Space Complexity: O(n), two recursive calls would add extra space for call stack

#problem 7

Compared to regular TrieNode, this one has a handler object. Router class has a RouteTrie object to hold all the routes
and have "/" as root route. handler is added to route with insert and route lookup is done by splitting the path on "/" and
then use Trie found operation. Both add_handler and lookup splits the route first and then traverses the nodes children. 

Edited after review: Both insert and lookup splits up the route and recursively navigate from roots to other nodes.
Since Trie nodes are saved as dictionary the containment check would require constant time lookup thus O(1)

Time Complexity: O(1) , as size of input path doesnt change the insertion of node  or lookup time of route that much.
Space Complexity: O(n)