# Graphs

In the past, when I've tackled the graph problem without due research, I've naively modeled as such:
An Area contains Rooms
A Room has contents, and doors to other Rooms

(This is generally how MUD style systems have addressed the issue since the early 1990s.)

This is all well and good, but it doesn't provide sufficient structure on its own to carry out some fairly basic tasks, such as "How do I search through a set of rooms methodically until I find the exit to the area?"

If all rooms have uniform types of exits (for example: n, s, e, w), then we could set some rules like "Go north first" or "try exits in a clockwise order". But this breaks down entirely when we look at the formal definition of graphs, which can have an arbitrary number of edges per node.

So let's back up:
A graph consists of nodes, which are connected by edges. 
An edge connects exactly two nodes (although it's possible each end connects to the same node)

Graphs can be directed or undirected. For example, a LAN would be undirected (if machine A can see B, then B can see A) while highways and streets are directed (some streets are two way, others are one way)

The two ways we'll look at modeling a graph are:
- adjacency matrix
- adjacency list

A matrix is an N-dimensional array (here we're thinking of a 2d array). We've previously touched on matrix multiplication as the math used to determine the angle at which the camera in a 3d scene views a polygonal surface (the 'normal vector') and this can be briefly sketched.

An adjaceny matrix consists of a 2 dimensional array (we may use arraylist/vector for convenience) where each x and y index refers to a specific node. 

So we'll want to make a numbered list of nodes, for example given the graph (directed, bidirectional)

a - b - c
     \
      d

We might create the list N = {"a", "b", "c", "d"} where node a is at index 0, etc.

The adjacency matrix lists a 1 in the intersections where nodes have connected edges, 0 where they do not.

    a b c d
    0 1 2 3
    -------
a 0|0 1 0 0
b 1|1 0 1 1
c 2|0 1 0 0
d 3|0 1 0 0

Reading this, we can see that b is adjacent to a, c, and d, and that a, c, and d are only adjacent to b.

If the connection from d was one way (from b->d but not d->b), then the bottom row would be all zeroes.

----
ADJACENCY LIST

we've spent some time in the past theorizing about what combinations of data structures might be useful
(there's probably no limit to the # of useful combinations), so let's look at another.

An Adjacency List is an array (arraylist) where each element contains a linked list.
(In structure, this is similar to a chaining hash table, although it's used totally differently.)

Like the adjacency matrix, each node is assigned an index, and the linked list contains the indices of the nodes which are connected to that node.

Same graph as above. N = {"a", "b", "c", "d"}, so a=0, b=1, c=2, d=3.

0 -> 1
1 -> 0, 2, 3
2 -> 1
3 -> 1

Remember:
With the adjacency matrix, it's 1=true, 0=false that the x and y nodes share an edge.
With the adjacency list, the linked list per node contains the indices of nodes with which it shares an edge.

