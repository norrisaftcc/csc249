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

