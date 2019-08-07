The program has two functions to provide merge/union of two singly linked list.

Union method creates two copies of each list, where each copy takes 0(n) for n items in the list.
Then appends two copies one after another, so overall complexity.

Intersection method goes through first list and for each element in it,
compares it against every element in the other list, which takes 0(n*2).
Then removing the duplicates from the resultant list takes another 0(n*2)

Time complexity : Union takes O(2*n) ~ O(n), Intersection takes O(n*2)
Space complexity: O(n), for each copy of list