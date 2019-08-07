For each group object, it contains a set of users and subgroups. 
 Data structures have been modified to set to store unique elements.
 If user belongs to user set of group , true is returned. otherwise
 if the group has non-empty set of groups, it recursively iterates the set of
 groups to check if user belongs to any of the group.

The worst case time complexity would be O(m * n) where m is the number of groups
and n is number of users.

Time complexity : O(mn)
Space complexity: O(n)