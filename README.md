# Data Structures & Algorithms in Python

A practical repository for learning and implementing **Data Structures and Algorithms using Python**.

This repository contains concepts, implementations, examples, and practice problems for beginners who want to build a strong foundation in Data Structures and Algorithms (DSA).

---

## 📚 Topics Covered

### 1. Array

Arrays are used to store multiple elements in a single collection.

**Concepts:**

* Array creation
* Accessing elements
* Traversing an array
* Insertion
* Deletion
* Updating elements
* Searching
* Finding maximum/minimum
* Reverse an array

**Example:**

```python
arr = [10, 20, 30, 40, 50]

print(arr[0])
print(arr)
```

---

### 2. String

A string is a sequence of characters.

**Concepts:**

* String creation
* Indexing
* Slicing
* Traversal
* String reversal
* Palindrome
* Character counting
* Anagram
* String searching

**Example:**

```python
text = "Hello"

print(text[0])
print(text[::-1])
```

---

### 3. Linked List

A Linked List is a linear data structure where elements are stored in nodes.

Each node contains:

* Data
* Reference/Pointer to the next node

**Types:**

* Singly Linked List
* Doubly Linked List
* Circular Linked List

**Operations:**

* Create
* Insert
* Delete
* Search
* Traverse
* Update

**Example structure:**

```text
10 → 20 → 30 → 40 → None
```

---

### 4. Stack

A Stack follows the **LIFO (Last In, First Out)** principle.

```text
       ┌────┐
       │ 30 │ ← TOP
       ├────┤
       │ 20 │
       ├────┤
       │ 10 │
       └────┘
```

**Operations:**

* Push
* Pop
* Peek
* Is Empty

**Example:**

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()

print(stack)
```

---

### 5. Queue

A Queue follows the **FIFO (First In, First Out)** principle.

```text
FRONT                         REAR
  ↓                             ↓
10 → 20 → 30 → 40
```

**Operations:**

* Enqueue
* Dequeue
* Front
* Rear
* Is Empty

**Types:**

* Simple Queue
* Circular Queue
* Priority Queue
* Deque

**Example:**

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()

print(queue)
```

---

### 6. Hash Table

A Hash Table stores data using **key-value pairs**.

Python's `dict` is an example of a hash table implementation.

**Concepts:**

* Hash function
* Hashing
* Collision
* Collision resolution
* Chaining
* Open Addressing
* Linear Probing
* Quadratic Probing

**Example:**

```python
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
```

---

### 7. Tree

A Tree is a non-linear hierarchical data structure.

**Components:**

* Root
* Node
* Edge
* Parent
* Child
* Leaf
* Subtree
* Height
* Depth

**Types:**

* Binary Tree
* Binary Search Tree
* AVL Tree
* Heap
* Trie

**Example:**

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40  60   80
```

---

### 8. Binary Search Tree (BST)

A Binary Search Tree follows this rule:

```text
Left subtree < Root < Right subtree
```

**Operations:**

* Insertion
* Searching
* Deletion
* Traversal

**Traversals:**

* Inorder
* Preorder
* Postorder

Example:

```text
          50
        /    \
      30      70
     /  \    /  \
   20   40  60   80
```

**Inorder Traversal:**

```text
20 → 30 → 40 → 50 → 60 → 70 → 80
```

---

### 9. Heap

A Heap is a complete binary tree commonly used to implement priority queues.

**Types:**

* Min Heap
* Max Heap

**Min Heap:**

```text
          10
        /    \
      20      30
     /  \
   40   50
```

**Max Heap:**

```text
          50
        /    \
      40      30
     /  \
   20   10
```

Python provides heap functionality through the `heapq` module.

```python
import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)

print(heapq.heappop(heap))
```

---

## 🔍 Searching Algorithms

Searching is used to find an element in a data structure.

### Linear Search

Checks elements one by one.

**Time Complexity:**

```text
Best Case:    O(1)
Worst Case:   O(n)
```

### Binary Search

Works on a **sorted array** and repeatedly divides the search space into two halves.

**Time Complexity:**

```text
Best Case:    O(1)
Worst Case:   O(log n)
```

---

## 🔄 Sorting Algorithms

Sorting arranges elements in ascending or descending order.

Algorithms covered:

* Bubble Sort
* Selection Sort
* Insertion Sort
* Merge Sort
* Quick Sort
* Heap Sort

### Complexity Overview

| Algorithm      |       Best |    Average |      Worst |
| -------------- | ---------: | ---------: | ---------: |
| Bubble Sort    |       O(n) |      O(n²) |      O(n²) |
| Selection Sort |      O(n²) |      O(n²) |      O(n²) |
| Insertion Sort |       O(n) |      O(n²) |      O(n²) |
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort     | O(n log n) | O(n log n) |      O(n²) |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) |
