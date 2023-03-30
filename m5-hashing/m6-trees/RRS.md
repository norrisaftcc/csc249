# Runway Reservation System
## From MIT 6.006 FA11

Assume an airport with a single runway. 
Our problem is to reserve times for future landings. 

Add time t to the set R of landing times IF no other landings are scheduled within k minutes
(for example, k=3 minutes. k might vary based on weather.)

Reserving a landing time means inserting into the set if the constraint is satisfied.

as t increments, check the data structure and remove times as they have passed.

Our performance goal:
O(lg n) time, where n is the size of the set (|R| = n)

Example of use:
with k=3

now 37, 41.2, 49, 56.3
insert 53 -> OK
insert 44 -> not allowed (too close to 41.2)
insert 20 -> not allowed (in the past)

--
Proposing to use all the data structures we know, and then ruling them out
(with audience interaction)
1. unsorted list/array
	- every action is O(n)
2. sorted array
	- binary search means finding items is O(lg n) , so that's good
	- ex. to insert 34, i can find the 'insertion point' (the value below it, and above it)
	- now i look at both of those and do the k-constraint check
	- but insertion is O of what?
	formally:
	- it can find the smallest i such that R[i] >= t in O(lg n) time
	- compare R[i] and R[i-1] in O(1) time
	- but insertion is linear time since it requires shifting items to make room

3. Linked list
	- insertion is constant time
	- search is ...?

4. Heaps (not yet coverd) - minheaps, maxheaps
	- an array that you can visualize as a tree
	- the <=k or >=k from t check is O(n) time with a heap

5. Hash Table / Dictionary
	- good insertion time and search time
	- but the <=k or >=k from t check is O(n) time with a dictionary

Our pipe dream:
	- if we could do fast insertion into
	- a sorted array
then we would meet all of our constraints.

This is what BSTs do for us.

Binary Search Tree invariant:
	for all nodes x:
	- if y is in the left subtree of x, key(y) <= key(x)
	- if y is in the right subtree of x, key(y) >= key(x)


now model RRS with BST:
- insert
- check
- delete


