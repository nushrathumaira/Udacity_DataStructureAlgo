find_files method is given a path and file suffix,
which then recursively goes through all directories and subdirectories
to find file names that have the suffix as file extension
and add the name to a list.
If we think of traversing the directory for given file suffix as a depth first traversal where the recursive function goes through each subdirectory every time, then time complexity is O(n) where n s the number of nodes or subdirectories. Insertion of file name should take constant O(1) time.

Time complexity : O(n) , n as count of subdirectories
Space complexity : O(n)