# sample questions

## some chatgpt ideas

We've looked at a sample question, the Runway Reservation System. This is a sample question for a data structures problem set. Kindly list three other sample questions for a data structures problem set. The proficiency level is second or third semester computer science students. The possible topics are: linked lists, stacks, queues, binary search trees, grids, and graphs.

Sure, here are three sample questions for a data structures problem set for second or third semester computer science students:

    Implement a queue data structure using a linked list. The queue should have the standard enqueue and dequeue operations, as well as a method to check if the queue is empty.

    Write a program that uses a stack to evaluate a postfix expression. The input expression will be given as a string, and should consist of integers and arithmetic operators (+, -, *, /). Your program should return the result of the expression.

    Implement a graph data structure using an adjacency list. The graph should have methods to add vertices and edges, and to perform a depth-first search (DFS) and breadth-first search (BFS) traversal. Your implementation should be able to handle graphs with cycles.

FTCC Programming Examples
List five other sample questions along these lines. 

Here are five more sample questions for a data structures problem set:

    Implement a binary search tree data structure with methods to insert a new node, search for a node with a given key, and delete a node with a given key.

    Write a program that uses a stack to check if a given string of parentheses is balanced. The input string will consist of only parentheses ('(', ')', '{', '}', '[', ']'). Your program should return true if the string is balanced (i.e., each opening parenthesis has a corresponding closing parenthesis), and false otherwise.

    Implement a hash table data structure using separate chaining to handle collisions. The hash table should have methods to insert a new key-value pair, retrieve the value associated with a given key, and delete a key-value pair.

    Write a program that uses a graph data structure to find the shortest path between two nodes in an undirected, weighted graph. The graph will be given as an adjacency list, where each vertex is represented by a list of its adjacent vertices and their associated weights. Your program should return the shortest path and its length.

    Implement a queue data structure using two stacks. The queue should have the standard enqueue and dequeue operations, as well as a method to check if the queue is empty. Your implementation should have O(1) amortized time complexity for enqueue and dequeue operations.

FTCC Programming Examples
kindly expand the binary search tree, stack, and graph questions to full assignments, including instructions and rubric.

Sure! Here are full assignments for the three questions I previously listed.

Assignment 1: Binary Search Tree

Instructions:

    Implement a binary search tree data structure with methods to insert a new node, search for a node with a given key, and delete a node with a given key.
    You should implement the BST as a Python class called BinarySearchTree.
    The BinarySearchTree class should have the following methods:
        insert(key, value): inserts a new node with the given key and value into the BST.
        search(key): returns the value associated with the given key, or None if the key is not in the BST.
        delete(key): removes the node with the given key from the BST.
        size(): returns the number of nodes in the BST.
    You may assume that all keys are unique.
    Your implementation should have O(log n) time complexity for insert, search, and delete operations, where n is the number of nodes in the BST.

Rubric:

    Correct implementation of BinarySearchTree class: 50 points
    Correct implementation of insert method: 20 points
    Correct implementation of search method: 15 points
    Correct implementation of delete method: 15 points
    Efficient implementation with O(log n) time complexity: 10 points

Assignment 2: Stack

Instructions:

    Write a program that uses a stack to check if a given string of parentheses is balanced. The input string will consist of only parentheses ('(', ')', '{', '}', '[', ']'). Your program should return true if the string is balanced (i.e., each opening parenthesis has a corresponding closing parenthesis), and false otherwise.
    You should implement the stack as a Python class called Stack.
    The Stack class should have the following methods:
        push(item): adds the given item to the top of the stack.
        pop(): removes and returns the top item from the stack.
        peek(): returns the top item from the stack without removing it.
        is_empty(): returns True if the stack is empty, and False otherwise.
    Your program should use the Stack class to check if the input string is balanced.
    You may assume that the input string is non-empty.

Rubric:

    Correct implementation of Stack class: 50 points
    Correct implementation of push method: 10 points
    Correct implementation of pop method: 10 points
    Correct implementation of peek method: 10 points
    Correct implementation of is_empty method: 10 points
    Correct implementation of string balancing using stack: 10 points

Assignment 3: Graph

Instructions:

    Write a program that uses a graph data structure to find the shortest path between two nodes in an undirected, weighted graph. The graph will be given as an adjacency list, where each vertex is represented by a list of its adjacent vertices and their associated weights. Your program should return the shortest path and its length.
    You should implement the graph as a Python class called Graph.
    The Graph class should have the following methods:
        add_vertex(vertex): adds the given vertex to the graph.
        add_edge(vertex1, vertex2, weight): adds an edge between the given vertices with the given weight.
        shortest_path(start_vertex, end_vertex): returns a tuple containing the shortest path from the start vertex to the end vertex and its length.
    You may assume that the graph is connected.
    Your implementation should use Dijkstra's algorithm to find the shortest path.

Rubric: