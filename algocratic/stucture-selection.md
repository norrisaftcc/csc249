# Structure Selection Guide

## “I Need This” → “Use That”

-----

> *Vocabulary is thought potential. Knowing which word to use is half the problem.*

-----

## Quick Decision Matrix

|“I need to…”                    |Use a…   |Why                              |
|--------------------------------|---------|---------------------------------|
|Undo operations in reverse order|**Stack**|LIFO: last action undone first   |
|Process items in arrival order  |**Queue**|FIFO: fair, ordered processing   |
|Fast search AND fast insert     |**BST**  |O(log n) for both (if balanced)  |
|Reverse a sequence              |**Stack**|Push all, pop all = reversed     |
|Buffer between producer/consumer|**Queue**|Decouples speeds, maintains order|
|Maintain sorted data dynamically|**BST**  |In-order traversal = sorted      |
|Match opening/closing delimiters|**Stack**|Most recent opener matches first |
|Breadth-first traversal         |**Queue**|Process level by level           |
|Organize hierarchical data      |**Tree** |Natural parent-child structure   |

-----

## Side-by-Side Comparison

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                        STACK vs QUEUE vs BST                                  │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│   STACK (LIFO)              QUEUE (FIFO)            BST (Binary Search Tree) │
│                                                                               │
│   ┌───┐                                                    50                 │
│   │ C │ ←top               ┌─────────────┐                /  \                │
│   ├───┤                    │ A → B → C   │               30   70              │
│   │ B │                    └─────────────┘              /  \    \             │
│   ├───┤                    front→    ←rear             20  40   80            │
│   │ A │                                                                       │
│   └───┘                                                                       │
│                                                                               │
│   Add: push to top         Add: enqueue to rear      Add: insert in order    │
│   Remove: pop from top     Remove: dequeue front     Remove: complex (3 cases)│
│                                                                               │
│   Order out: C, B, A       Order out: A, B, C        In-order: 20,30,40,50...│
│   (reversed)               (preserved)               (sorted)                 │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│   OPERATIONS              OPERATIONS                 OPERATIONS               │
│   push(x)   O(1)          enqueue(x)  O(1)          insert(x)   O(log n)*    │
│   pop()     O(1)          dequeue()   O(1)*         search(x)   O(log n)*    │
│   peek()    O(1)          front()     O(1)          delete(x)   O(log n)*    │
│   empty()   O(1)          empty()     O(1)          min/max()   O(log n)*    │
│                                                                               │
│                           *O(1) with circular buffer *When balanced           │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│   BEST FOR:               BEST FOR:                  BEST FOR:                │
│   • Undo systems          • Task scheduling          • Sorted data            │
│   • Backtracking          • Print queues             • Fast search + insert   │
│   • Delimiter matching    • BFS traversal            • Range queries          │
│   • Expression eval       • Buffering                • Ordered iteration      │
│   • Call stack mgmt       • Fair processing          • Hierarchical data      │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘
```

-----

## The Critical Distinctions

### Stack vs Queue: Where Do Items Exit?

```
                STACK                           QUEUE
                
   Input:  A, B, C                    Input:  A, B, C
                
   Same end ──┐    ┌── Same end       Different ends
              ↓    ↑                        ↓                    ↓
            ┌───┐                    ┌─────────────────────────────┐
            │ C │                    │ A        B        C         │
            │ B │                    └─────────────────────────────┘
            │ A │                      ↑                           ↑
            └───┘                    exit                        enter
              ↑                      (dequeue)                 (enqueue)
           exit & enter
           (push & pop)              Output: A, B, C
                                     (same order)
   Output: C, B, A                   
   (reversed order)                  
```

**The question:** Do you need items in the *same* order or *reversed* order?

### Linear vs Hierarchical: One Dimension or Many?

```
LINEAR (Stack/Queue):                HIERARCHICAL (Tree):

Items in a line                      Items in levels with relationships

A → B → C → D                              A
                                          / \
One predecessor, one successor           B   C
                                        / \   \
                                       D   E   F

                                     One parent, multiple children
```

**The question:** Is your data a sequence or a hierarchy?

### Array-Backed vs Node-Based: Memory Trade-offs

```
ARRAY-BACKED:                        NODE-BASED (Linked):

[A][B][C][_][_]                      A → B → C → ∅

✓ Cache-friendly (contiguous)        ✓ Easy insert/delete
✓ No pointer overhead                ✓ Dynamic size
✗ May need resize                    ✗ Pointer overhead
✗ Insert/delete may shift            ✗ Cache unfriendly
```

**The question:** Do you prioritize memory efficiency or structural flexibility?

-----

## Common Mistake Patterns

### Mistake 1: Using Stack When You Need Queue

```
SYMPTOM: "My task scheduler isn't fair—tasks added first are done last!"

PROBLEM: You used a stack (LIFO) instead of a queue (FIFO)

FIX: Change push/pop to enqueue/dequeue
```

### Mistake 2: Using Queue When You Need Stack

```
SYMPTOM: "My undo button undoes the oldest action, not the most recent!"

PROBLEM: You used a queue (FIFO) instead of a stack (LIFO)

FIX: Change enqueue/dequeue to push/pop
```

### Mistake 3: Linear Search When Tree Would Help

```
SYMPTOM: "Searching my sorted list is slow—I have to check every element!"

PROBLEM: Linear search in list is O(n)

FIX: Use a BST for O(log n) search, or binary search on sorted array
```

### Mistake 4: Using BST When Hash Table Would Be Better

```
SYMPTOM: "I just need to check if something exists, and BST feels slow"

PROBLEM: BST is O(log n), but hash table is O(1) for lookup

FIX: If you don't need ordering, consider a hash table (coming in Week 13)
```

-----

## Translation Patterns: Python ↔ C++

### Stack

|Python           |C++                              |
|-----------------|---------------------------------|
|`stack = []`     |`std::stack<T> stack;`           |
|`stack.append(x)`|`stack.push(x);`                 |
|`stack.pop()`    |`T x = stack.top(); stack.pop();`|
|`stack[-1]`      |`stack.top()`                    |
|`len(stack) == 0`|`stack.empty()`                  |

**Gotcha:** C++ `pop()` returns `void`, not the element!

### Queue

|Python                         |C++                                |
|-------------------------------|-----------------------------------|
|`from collections import deque`|`#include <queue>`                 |
|`queue = deque()`              |`std::queue<T> queue;`             |
|`queue.append(x)`              |`queue.push(x);`                   |
|`queue.popleft()`              |`T x = queue.front(); queue.pop();`|
|`queue[0]`                     |`queue.front()`                    |
|`len(queue) == 0`              |`queue.empty()`                    |

**Gotcha:** Python `list.pop(0)` works but is O(n). Use `deque.popleft()`.

### BST Nodes

|Python            |C++                                         |
|------------------|--------------------------------------------|
|`node.left = None`|`node->left = nullptr;`                     |
|`if node is None:`|`if (node == nullptr)`                      |
|`self.left`       |`this->left` (or just `left`)               |
|Garbage collected |Must manually `delete` or use smart pointers|

**Gotcha:** C++ requires explicit memory management. Forgetting = memory leaks.

-----

## Visualization Mental Models

### Stack: Cafeteria Plates

```
        ↓ push
    ┌─────────┐
    │  plate  │ ← take (pop)
    ├─────────┤
    │  plate  │
    ├─────────┤
    │  plate  │
    └─────────┘
    
Can only access top plate.
Clean plates added to top.
Last plate placed = first plate taken.
```

### Queue: Checkout Line

```
    →→→ enter (enqueue)
    
    ┌────┬────┬────┬────┐
    │ D  │ C  │ B  │ A  │ →→→ exit (dequeue)
    └────┴────┴────┴────┘
    rear              front
    
First person in line = first person served.
New people join at rear.
```

### BST: Family Tree With Rules

```
              Grandparent (50)
             /              \
    Younger (30)         Older (70)
       /    \                  \
   (20)    (40)               (80)
   
Every left child < parent.
Every right child > parent.
To find someone: "Are you older or younger than X?"
```

-----

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                  WHEN TO USE WHAT                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Need LIFO (reverse order)?                                     │
│  → STACK: push/pop from same end                                │
│                                                                 │
│  Need FIFO (preserve order)?                                    │
│  → QUEUE: enter rear, exit front                                │
│                                                                 │
│  Need fast search + insert + sorted order?                      │
│  → BST: O(log n) operations when balanced                       │
│                                                                 │
│  Need O(1) lookup by key (no ordering)?                         │
│  → HASH TABLE (Week 13)                                         │
│                                                                 │
│  Need to model relationships between entities?                  │
│  → GRAPH (Week 14)                                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  REMEMBER: The structure you choose shapes how you think        │
│  about the problem. Choose the word that fits the concept.      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

-----

*Ontological Studies Division — Know Your Structures, Know Your Options*