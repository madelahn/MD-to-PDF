\newpage# 0 - Running Time Analysis


**Time complexity** - The number of steps an algorithm will take with an input of size $n$.

- **Steps:** Arithmetic operations, comparison operations, and data movement operations all take constant time.

- **Input Size:** Number of elements, number of edges + vertices, and number of bits.


#### Worst-Case Time Complexity
Let $A$ be an algorithm, and let $t(x)$ be the number of steps taken by $A$ on input $x$. The **worst-case time complexity** of $A$ is a function $T(n)$ such that:
$$T(n) = \max(t(x)) \equiv \max\{t(x): x \text{ input of } n\}$$
With worst-case time complexities, we have **upper bounds:**
$$T(n) \leq g(n),$$ and **lower bounds:**
$$T(n) \geq g(n)$$
To prove that the inequality is true for each, let $c$ be some constant and $e$ be an element of set $S$ of the time complexities for all inputs. We write:
$$\max(S) \leq c \iff \forall e \in S: e \leq c$$
$$\max(S) \geq c \iff \exists e \in S: e \geq c$$
However, note that constants ($\mathbb{N}$) in runtime can vary between machines. Hence, we assume that runtimes occur **within a constant factor**. Additionally, to use "for every" when talking about input sizes can be redundant since we primarily care about large input sizes. Therefore, we can instead say **"for sufficiently large $n$"**.

Then, we can finally get our **Big-O** and **Omega** bounds for a worst-case time complexity:
$$T(n) \text{ is } O(g(n)) \iff \exists c > 0, \exists n_0 > 0 \text{ such that } \forall n \geq n_0: T(n) \leq c\cdot g(n)$$
$$T(n) \text{ is } \Omega(g(n)) \iff \exists c > 0, \exists n_0 > 0 \text{ such that } \forall n \geq n_0: T(n) \geq c \cdot g(n)$$


###### Theta Bounds
What if $T(n) = O(g(n)) = \Omega(g(n))$? 
> Then, we get a **Theta Bound ($\Theta(g(n))$)**.

To prove Theta bounds, by definition, we must show that $O(g(n)) = \Omega(g(n))$. That is, for every input of size $n$, the algorithm takes at most $c_1 \ n^2$ steps, **and** there exists an input of size $n$ for which the algorithm takes at least $c_2 \ n^2$ steps.

# 1 - Abstract Data Types


**Abstract Data Type -** Describes an object and its operations
**Data Structure** - Some specific implementation of an abstract data type.

### Priority Queues

> **Example of ADT:** Priority Queue
> 	**Object:** Set $S$ of elements with 'keys' ('priority') that can be compared.
> 	**Operations:**
> 		- `Insert(S, x)`: Insert element $x$ in $S$.
> 		- `Max(S)`: Returns an element of highest priority in $S$.
> 		- `Extract_Max(S)`: Returns Max($S$) and removes it from $S$.
> *Application:* Priority queues can be used to maintain a set of jobs and schedule them according to their priorities:
> 	- When a new job arrives, insert.
> 	- When a processor becomes available to execute a job, extract and assign the job to the free processor.


#### Data Structures for Implementing Priority Queues
| Worst Case Time For   | Insert      | Extract_Max |
| --------------------- | ----------- | ----------- |
| Unordered Linked List | $\Theta(1)$ | $\Theta(n)$ |
| Ordered Linked List   | $\Theta(n)$ | $\Theta(1)$ |
These are not efficient, we want a smaller time complexity when computing these operations.
The goal is to achieve a data structure that can do each operation in at most $\Theta(\log n)$ time (the most efficient time).

##### Max-Heaps
**Complete Binary Tree (CBT) -** A binary tree where for every level $l$, except maybe the bottom level. has $2^l$ nodes. All nodes in the bottom level are as far left to the possible.
	The height of the tree is the number of edges in the longest path from root to leaf. 
	For a CBT with $n$ nodes, the height is always $\lfloor \log_2n\rfloor$.

The $n$ elements of Max-Heaps are stored in a complete binary tree with $n$ nodes such that the **Max-Heap Property** hold:
$$\text{Priority of each node } \geq \text{ Priority of its children}$$
> **Example:** $S = \{3,4,5,7,7,9,9,12,17\}$



###### Array Representation of Heaps
Max heaps can be stored in arrays from indices $1$ to $n$ alongside a variable for the heap-size.

> **Example:** $A = [17, 9, 12, 6, 6, 9, 5, 3, 4]$; A.Heapsize = 9

But then, how do we point to other values within the heap? For example, take $A[2] = 9$; we know its two children are at indices 4 and 5. More formally,
$$\text{Left child of } A[i] \text{ is } A[2i]$$
$$\text{Right child of } A[i] \text{ is } A[2i + 1]$$

  Similarly,
  $$\text{Parent of } A[i] \text{ is } A[\left\lfloor i/2\right\rfloor]$$

###### Heap Operations
For the three operations `Insert`, `Max`, and `Extract_Max`, we want to maintain the **CBT shape** and maintain the **max-heap property**.

`Insert(A, x)`: Increment `A.Heapsize` and the size of the array by 1, then put in the bottom-left most node. If $x$ is greater than its parent, swap spots with its parents until the max-heap property is satisfied or until $x$ is the root. The amount of times we must swap must be at most the height of the CBT ($\lfloor \log_2n\rfloor$).
> $O(\log n)$; For every input $A,x$ of size $n$, the algorithm takes at most $c_1 \cdot \log n$ steps. 
> $\Omega(\log n)$; For some $A,x$ of size $n$ the algorithm takes at least $c_2 \cdot \log n$ steps when the priority of $x$ is greater than the priority of the root. 
> Hence, the worst-case complexity is $\Theta(\log n$).

`Max(A)`: Time complexity is always constant $\Theta(1)$ since we know it's always in the first index.

`Extract_Max(A)`: Return the first index of the array and move the last index to the first so that the heap decreases by 1. To maintain max-heap property, compare the root with its children nodes and swap with the higher-priority child. Continue to do this until the node is higher priority with its children, or if it is a leaf (index of $x \leq \lfloor n/2 \rfloor$).
> $O(\log n)$ ; For every input $A,x$ of size $n$, the algorithm takes at most $c_1 \cdot \log n$ steps.
> $\Omega(\log n)$; For some input $A,x$ of size $n$, the algorithm takes at least $c_2 \cdot \log n$ steps when $A[A.heapsize]$ has the smallest priority. 
> Hence, the worst-case complexity is $\Theta(\log n)$.



##### Application - HeapSort
To sort an array $A$ of $n$ elements:

- Make a heap out of the elements of $A$ (takes $\Theta(n$) time).

- `Extract_Max(A)` $n$ times (takes $\Theta(\log n)$ time each extraction).
Hence, the worst-case time complexity is $\Theta(n \log n)$.
This sorting can be done in-place; *see CLRS 6.4*.


### Binomial Heaps
The issue with priority queues is that it doesn't allow unions (e.g., what if we want to merge two queues together for one CPU?). Instead, we can create **mergeable priority queues** called the minimum binomial heap. All operations will take $O(\log(n))$ time.


##### Binomial Trees

- $B_k$ tree: Defined recursively.
For $k=0$, it is $1$ node with $0$ subtrees. For $k \geq 1$, the tree has $2^k$ nodes with $k-1$ subtrees.

![Pasted image 20230918131549.png](C://Users/madeline/Documents/GitHub/Obsidian/Courses/3rd Year/Fall/CSC263/Images/Pasted image 20230918131549.png)
Looking at the depth of reach tree (starting at $0$), we see that the number of nodes at each depth is the binomial coefficient of the row. Hence, a $B_k$ tree has:

- Height $k$

- $2^k$ nodes

- $\binom{k}{d}$ nodes at depth $d$


##### Binomial Forests
**Binomial Forest $F_n$ of size $n$**: A sequence of $B_k$ trees with ==strictly decreasing== $k$'s.
$F_n$ has $n$ nodes with $n = <b_t, b_{t-1}, ..., b_0>_2$, where $t = \lfloor \log_2 n \rfloor$.
$F_n$ will have all trees $B_i$ such that bit $b_i = 1$; Let $\alpha(n)$ be the number of 1's in binary representation of $n$. $F_n$ has $\alpha(n)$ trees, and $n - \alpha(n)$ edges.

> **Example: Binomial Forest $F_7$ of $n=7$**:
> $n = 7 = < 1 1 1 >_2 = 2^2 + 2^1 + 2^0$; so $F_7 = <B_2, B_1, B_0>$
> $F_7$ has $\alpha(7) = 3$ trees, and has $7 - \alpha(3) = 4$ edges.
> 
> **Example: Binomial Forest $F_9$ of $n=9$:**
> $n = <1 0 0 1>_2 = 2^3 + 2^0$; so $F_9 = <B_3, B_0>$
> $F_9$ has $\alpha(9) = 2$ trees, and has $9 - \alpha(9) = 7$ edges.


#### Minimum Binomial Heaps
**Minimum Binomial Heap of $n$ elements** is a **Binomial Forest $F_n$** such that:

- Each node of $F_n$ stores one element.

- Each $B_k$ tree of $F_n$ is min-heap ordered.

> **Example:**
> Suppose we have $S = \{10, 13,1,3,8,18,7\}$, with $n = 7$ elements.
> Put $S$ in $F_7 = <B_2 B_1 B_0>$. Lower numbers are put at the roots of each binomial tree.
> It will take $4$ comparisons, the number equal to the number of edges in the binomial forest (i.e., ==one key-comparison per binomial heap edge==).


##### Storing Binomial Heaps in Memory
Each node can have a different number of children, but we can't point to multiple children. Instead, each node has a **parent pointer**, a **left-child pointer**, and a **right-sibling pointer** (i.e., same parent). Additionally, we use sibling pointers to connect trees as well as a HEAD pointer to begin iteration through the forest. Note that each node has at most 3 pointers.
> We will primarily going through edges rather than pointers.


##### Binomial Heap Operations
>**Lemma 1:** We can merge two min heap-ordered $B_k$ trees into a single min heap-ordered $B_{k+1}$ tree with just one key comparison, i.e., to merge two trees with roots $x, y$; if $y < x$, put the smaller tree on top.
>
>**Lemma 2:** Deleting the root of a min heap-ordered $B_k$ tree gives a min binomial heap (i.e., a forest of min binomial heaps).


###### **Union(T,Q)**
Let $T$ be a binomial heap of size $n=3 = <1 1>_2$, and $Q$ be a binomial heap of size $n = 7 = <1 1 1>_2$.
Similarly to binary addition, we add each binary tree and carry into the next column. So, $T + Q = S = <B_4 B_2>_2$.
The union will add 3 edges and take $3$ key-comparisons.

**Worst-Case Complexity of Union(T,Q)** - Suppose $|T| \leq n$ and $|Q| \leq n$. Each of $T,Q,$ have $O(\log n)$ $B_k$ trees $\implies$ Union(T, Q) takes at most $O(\log n)$ key-comparisons.


###### Insert(T,x)
Let $(T,x)$ be a trivial binomial tree of size $1$ and $x$ is the element we want to insert. Then, we go through the same process as the Union to insert $x$. Then, Insert(T, x) takes at most $O(\log n)$ key-comparisons.


###### Min(T)
Scans the roots of the $B_k$ trees to return the smallest key.


###### Extract_Min(T)
When we remove the root (min) of the forest, we locate the smallest element, then delete the root. We are left with two binomial heaps, which we can then take the Union of to create a new binomial heaps. Hence, it takes $O(\log n)$ time.


###### Other Operations
Given a pointer to a node $x$ in a binomial heap $T$, we can do the following:

- Decrease_Key(T, x, k): Decrease the key at node $x$ to $k$.
	- We can simply swap with the parent, taking $\log(n)$ time.

- Remove(T, x): Remove the key at node $x$.
	- Completed in $\log(n)$ time.

- Increase_Key(T, x, k)

**Cost of $k$ Successive Inserts:** Suppose $T$ is a binomial heap with $n$ elements. What is the cost of $k$ successive inserts into $T$?
$$Insert(T, x_1), ..., Insert(T, x_2), ..., Insert(T, x_k)$$
$$O(\log n), O(\log_n +1), ..., O(\log n + k)$$
> **Example: Let $|T| = 27 = <11011>_2$:**
> $T = <B_4 B_3 B_1 B_0>$. Adding $x_k$ to $T$ does not always take the same number of key-comparisons; instead, we want to look at the ==average cost==. 
> Initially $T$ has $23$ edges, and after 5 insertions, we have $ 32 - 1 = 31$ edges.
> In total, the insertions took $31 - 23 = 8$ steps. **Why?**

**Claim:** If $k > \log_2 n$ the total cost is at most $2k$ key-comparisons.
**Proof:** A2-Q1
The average cost per insert is $\leq 2$ key-comparisons.



### Dictionary
**Object -** Set $S$ of keys
**Operations:**

- Search(S, x) - Returns elements with key $x$ if $x \in S$. Else, returns 'not found'.

- Insert(S, x) - Inserts $x$ in $S$.

- Delete(S, x) - Deletes $x$ from $S$.


##### Data Structure for Dictionaries - BST
**Linked List:**

- Insert: $\Theta(1)$

- Search: $\Theta(n)$

- Delete: $\Theta(n)$
This takes too long. Can we get this completed in $\Theta(\log n)$ time?


###### Binary Search Trees
For each node in a BST, the keys in the left subtree $\leq$ the node's key $\leq$ keys in the right subtree.

**In-Order Traversal**

- Traverse the node's left subtree recursively.

- Visit the node.

- Traverse the node's right subtree recursively.
In-order traversal of a BST visits keys in ascending sorted order.

**Is the BST for a set $S$ of keys unique?**
> No; suppose we have $S: \{2,4,5,6,7,9\}$. We can left-rotate the BST, and get $7$ as our root now. However, when we try to form this new structure, we see that the nodes $5,6$ need to go to the right of node $4$. Using this idea, we can show different ways BSTs can be drawn.


###### BSTs and Operations
Insert and Search are determined intuitively. However, the Delete operation is more difficult.
There are several possible cases:

- The node is a leaf - Just remove the leaf.

- The node has one child - Remove the node and replace it with the child (and its subtree).

- The node has two children - Find the 'successor' of the node. Go **one step** to the right, and then **all the way** down the left (to the leaf). After this, copy the successor's key into the original nodes, so we know it only has at most a right subtree (since we went down to the leaf).
	- By convention we use the 'successor', however, we can also use the 'predecessor' if we wanted to (it's just not standard).


##### Worst-Case Time Complexity
The worst-case time complexity of Search, Delete, and Insert, are all $\Theta($height of tree$)$.

- The maximum height of a BST with $n$ nodes is $n -1$.


### Balanced Binary Search Trees
When we insert multiple keys into a BST, the tree becomes quite right-heavy. Then, when we search, it'll take $\Theta(n)$ time. We want a way to keep this time complexity under $\Theta(\log n)$ time.


#### AVL Tree
Recall:

- height($v$): Number of edges in the longest path from $v$ to a leaf.

- height($T$): Height of the root node of $T$

- Height(1) = 0

- height(empty tree) = -1

**Balance Factor (BF)**
For a node $v$, the balance factor is the difference in weight between its two **subtrees**, that is:
$$BF(v) = h_R - h_L, \text { or the height of the right subtree - height of the left subtree }$$

**Adelson-Velski-Landis Trees** - A BST $T$ such that for every node $v \in T: -1 \leq BF(v) \leq +1$. Then:
$$BF(v) = \begin{cases}+1, & \text{Right heavy}\\
0, & \text{Balanced}\\
-1, & \text{Left heavy}\end{cases}$$
If $BF(v) \geq +2$, then it is considered right-heavy. If it is $\leq -2$, then it is left-heavy.


##### Properties of AVL Trees

- AVL trees of $n$ nodes has height $\Theta(\log n)$ (i.e., height $\leq 1.44 \cdot \log_2(n+2)$)

- Inserts and deletes can be done in $\Theta(\log n)$ time while maintaining tree balance.
AVL Trees are clean and simple, and are quite easy to use in practice.


##### AVL Trees Operations

###### **Search(T, x)**
Calculated the same way as regular BSTs, $\Theta(n)$.


###### Insert(T, x)
Generally, when we insert, make $x$ a leaf as with any BST with $BF(x) = 0$. Then, go up from $x$ to the root and, for each node:

- Adjust the balance factor.
	- $+1$ for each right-subtree, and $-1$ for each left-subtree.
	- If the adjusted BF is 0, then we're done.

- Rebalance if necessary ($BF > 1, BF < -1$).
	- If $BF(v) = +2$:
		- If $BF(v.right) = +1$, left-rotation, update BFs of rotated nodes; stop.
		- If $BF(v.right) = -1$, do right-left rotation, update BFs of rotated nodes; stop.
	- If $BF(v) = -2$, symmetric as for $+2$.

> **Example:** AVL of $\{1,3,7,12,14,17,19\}$
> Insert(T, 8): Goes into the left subtree from the root $12 \to 3 \to 7$, becoming a leaf. $8$ is the right subtree of $7$, meaning we increment $7$ and every parent node by $+1$. Then, the root $12$ becomes $-1$. We do not need to rebalance.
> 
> Insert(T, 5): $5$ goes to $7$ as a subtree. $7$ goes from a BF of $+1 \to 0$, so we do not need to update any of the parents' BFs, since we know it'll still be balanced.
> 
> Insert(T, 10): $10$ goes to the right of $8$. $BF(8) = +1, BF(7) = +1, BF(3) = +2$. $3$ and $7$ are too right-heavy to retain AVL properties. Then, we can **rotate** the subtree, and now $12$ has the left subtree $7$ instead of $3$. Hence, the root's left subtree becomes $0$ and is now rebalanced while still being a BST. Additionally, the height (2) is the same as before inserting $10$. Then, we can stop there.

> **Example:** AVL of $\{1,3,5,7,8,12,14,17,19\}$
> Insert(T, 6): $6$ gets added to the right subtree of $5$, resulting in an imbalanced left subtree. We can try to do a left-rotation around $3$, but the tree is still imbalanced. So, first do a right-rotation around $7$'s subtree so that $3$ now has a right-child of $5$ instead of $7$. After, we can do a left-rotation around $3$ so that the left subtree has a root of $5$ instead of $3$. Then, $BF(5)$ is rebalanced and a BST, and the height is also the same as before inserting $6$.

Hence, the total runtime is:

- $O(\log n)$ for inserting $x$ into $T$ as we do with usual BSTs.

- $O(\log n)$ for rebalancing to get a proper balance factor.
Insert can be completed in $O(\log n)$ time.


###### Delete(T, x)
Similarly to Insert, we take $O(\log n)$ time to remove $x$ into $T$ as we would with BSTs, and then another $O\log(n)$ time for rebalancing.
However, the height does not necessarily stay the same when deleting a node in an AVL tree; it could be smaller. You may need to take $\Theta(\log n)$ steps to rotate to balance, but since each rotation takes constant time, this is okay.

# 2 - Hash Tables


### Hash Tables

#### Dictionaries
Recall the definition of a dictionary:

- Dynamic set $S$ of items with keys that take from some universe $U$.

- We have the operations `Search`, `Insert`, `Delete`.

 There are two cases of $U$ that must be considered; big and small.

##### 1. Universe of Keys $U$ is Small
Suppose $U = \{0, 1, 2, ..., \mu - 1\}$, and $|U| = \mu$ is small.
To perform operations with $U$, use a **Direct Address Table** $T$.
Then, $T[0, ..., \mu - 1]$ of size $|U| = \mu$. Store the item with key $k \in U$ into $T[k]$.

Hence, each operation (`Insert`, `Delete`, `Search`) takes $\Theta(1)$ in worst-case time.

##### 2. $U$ is (Very) Large
> **Example:** Suppose $k$ is a social security number (SSN), and $k$ is any 64-bit integer (i.e., $|U| = 2^{64}$).

**Worst Case** - This is very bad!
Let $n$ be the number of keys in $S$, and $|n| < |U|$.
Let $m$ be the size of the hash table $T[0...m-1]$, where typically $n  = O(m$).
We have the **hash function** $h$:
$$\begin{aligned}U & \to \{0,1,2,..., m-1\}, \text{ and }\\
k \in U  & \to i \circ T[0 ... m-1], \text{ where } h(k) = i
\end{aligned}$$
Then, $T(k)$ hashes into slot $h(k)$.
Hashing puts items into a linked list (easier to delete) starting at index $i$.

Suppose for a hash table that we insert 3 keys $k_1, k_2, k_3$. We insert them into different indices of the table:

- $h(k_1) \to i$

- $h(k_2) \to j$

- $h(k_3) \to h(k_1) = i$
	- This is a **collision**, and will cause hashing with chaining.
By pigeonhole principle, there is bound to be multiple keys in one slot when $U$ is large; so what is an effective way to search for these keys?

###### Simple Uniform Hashing Assumption (SUHA)

- Every key $k \in U$ is equally likely to hash into any of the $m$ slots of $T$, independent of where other keys hash into.

- $P(h(k) = i) = \frac{1}{m} \forall i : 0 \leq i \leq m -1$.

Given an empty table $T$, enter $n$ keys.
The **expected** length of chain at any slot $i$ of $T$ is called the **load factor**, $\alpha = \frac{n}{m}$ because of SUHA.


###### Hash Table Searching (For Large $U$)
How many key comparisons does it take to do `Search(k)`? What is the expected $(E)$ cost?

- Suppose $k \not\in T[0..m-1]$. Then, $E \approx \alpha = \frac{n}{m}$.

- Suppose $k \in T[0..m-1]$. Then, $E \approx \frac{\alpha}{2} = \frac{n}{2m}$
Therefore, the expected cost of `Search(k)` is $\Theta(1 + \alpha) = \Theta(\alpha) = \Theta(\frac{n}{m})$.

**Another Note:**
>Suppose $n = 100$, and $\alpha \leq 3$. What is the value of $m$?
>	Since $\frac{n}{m} \leq 3$, $m \geq \frac{100}{3}$.
>	Then, $n \in O(m)$, so $n \leq c\cdot m$, and $\frac{n}{m} \leq c$.
>	
>	This is a popular hash function: $h(k) = k\mod p$, where $p$ is a prime number.
>	The keys that are chosen are equally likely to be chosen, even though hashing is technically a deterministic function.


##### Hash Table Operation Runtime Summary
The worst-case runtime of the three operations for a hash table:

| Operation | Small $U$   | Big $U$ |
| --------- | ----------- | ------- |
| `Insert`  | $\Theta(1)$ | $O(1)$  |
| `Delete`  | $\Theta(1)$ | $O(1)$  |
| `Search`  | $\Theta(1)$ | $O(n)$  |


### Bloom Filters
Bloom filters are space-efficient =="Probabilistic Dictionary"== that maintains the 'fingerprints' of the elements of a set $S$.

**Operations:**

- `BF_Insert(x):` $S \leftarrow S \cup \{X\}$

- `BF_Search(x):` $\begin{cases}\text{No} & \implies x \not\in S\\ \text{Probably} & \implies \text{Probably} x \in S\end{cases}$


#### Characteristics
Bloom Filters are arrays $BF[0, ..., m-1]$ of $m$ bits, initially all 0's.
We have $t$ independent hash functions $h_1, h_2, ..., h_t$, with:

- $h_i$: $U \to \{0, 1, ..., m-1\}$

- $h_i$ satisfying SUHA,
where SUHA is every element is equally likely to hash into any of the $m$ slots of the BF, independent of where other elements have been hashed to.

>**Example:** $BF[0...7]$ with $t = 2: h_1, h_2$.
>`BF_Insert(x1)`: We put $h_1$ and $h_2$ into different indices.
>`BF_Insert(x2)`: We put $h_1, h_2$ into different places.
*>	What happens if there are overlaps?*
>This is okay as long as the combination $h_1, h_2$ are unique, since $t = 2$.
>
>`BF_Search(x)`: Suppose $h_1$ has 1 and $h_2$ has 0. Then, it is not in the hash table (i.e., $x \not\in x_1, x_2$).
>`BF_Search(x)`: Suppose $h_1, h_2$ both have $1$, then it will probably be in the hash table(but can be a false positive).


###### Probabilities of False Positives
**Setup:**

- Insert $x_1, x_2, ..., x_n$ into an empty $BF[0 ... m-1]$, with $t$ independent hash functions $h_1, ..., h_t$ each satisfying SUHA.

- Do `BF_Search(x)` for $x \not\in x_1, ..., x_n$.
**Want to compute:**

- `P(False Positive) = P(BF_Search(x) = 'Probably Yes')`
**We first compute:**

- For an arbitrary index $i$ of `BF`, $P(BF[i] = 0)$ after inserting $x_1, ..., x_n$.

- With insertion of $x_1$, the probability of hitting $i$ is $\left(1 - \frac{1}{m}\right)^t$.
	-  This probability is the same for all $m$ keys. Hence, the probability is equal to $(1 - \frac{1}{m})^{nt}$.
More formally:

Consider an arbitrary index $i$ of the BF. After inserting:
$$\begin{aligned}
P(BF[i] = 0) & = P(\cap^n_{k=1} \cap^t_{j=1} h_j(x_k) \neq i)\\
& = \prod_{k=1}^n \prod_{j=1}^t P(h_j(x_k) \neq i)\\
& = \prod_{k=1}^n \prod_{j=1}^t \left(1 - \frac{1}{m}\right)\\
& = \left(1 -\frac{1}{m}\right)^{t\cdot n}
\end{aligned}$$
Note that $1 - y \approx e^{-y}$ for small $y = \frac{1}{m}$. Then, the probability is:
$$P(BF[i] = 0) \approx e^{-nt/m}$$

Then, the probability of $i$ being picked is:
$$\begin{aligned}P(BF[i] = 1) & = 1 - P(Bf[i] = 0)\\
& \approx 1 - e^{-nt/m}\end{aligned}$$

Hence:
>**Lemma 1.** After inserting $x_1, ..., x_n$ into a BF of size $m$ with $t$ hash functions, for every index $i$, $P(BF[i] = 1) \approx 1 - e^{-nt/m} = q$.


We can calculate $P($False Positive):
$$\begin{aligned}
P(\text{False Positive}) & = P(BF\_Search(x) = \text{Probably Yes})\\
& = P(BF(h_1(x)) = 1 \cap BF(h_2(x) ) = 1 \cap \ ...  BF(h_t(x)) = 1)
\end{aligned}$$
Note that these events are not independent, but they to approximate to be independent. Hence:
$$\begin{aligned}
P(\text{False Positive}) & \approx P(BF(i_1)) = 1 \cdot P(BF(i_2)) = 1 \cdot \ ... \ \cdot P(BF(i_t)) = 1\\
& \approx q^t\\
& = \left(1 - e^{-nt/m}\right)^t
\end{aligned}$$
We fix the ratio $\frac{m}{n}$ (the number of bits per element), and then find $t$ (i.e., the number of hash functions) which minimizes $P$(False Positive). We get the optimal $t$:
$$t = (\log_e 2) \frac{m}{n} = 0.69 \frac{m}{n},$$
Therefore, we can simplify our probability to get:
$$P(\text{False Positive}) = 0.62^{m/n}$$


#### Application: Malicious URLs
Suppose a web browser wants to check if a URL entered by a user is malicious or not, with 10 million URLs in $S$, with $S \approx 500$ MB total. We don't want to store a file size this large on the user side, so we can store only a **Bloom Filter** of $S$ on the user side.
To check if a URL is in $S$:
$$\text{BF\_Search(URL)} = \begin{cases}\text{No} & \implies \text{URL} \not\in S\\ \text{Probably} & \implies \text{Probably URL} \in S. \text{Issue a warning} \end{cases}$$
We can allocate $8$ bits per URL, so our size of $BF$ is $8n = 8 \cdot 10 \text{ million bits} \approx 10MB$. The $t$ that minimizes $P(\text{false positive})$ is:
$$t \approx 0.69\frac{m}{n} = 0.69 \cdot 8 = 5.52 \text{ hash functions}$$
We can't use a fraction of a hash function, so we round up and therefore use $6$ independent hash functions.
With this $t$: $$P(\text{false positive}) \approx 0.62^{m/n} = 0.62^8 \approx 2\%$$



# 3 - Randomized Quicksort


### Randomized Quicksort Algorithm
**Input:** A set $S$ of $n$ distinct keys.
**Output:** The keys of $S$ in increasing order.
We have `RQS(S)`, which is a recursive, divide-and-conquer algorithm.

- If $S$ is empty, then return.

- If $|S| = 1$, then output the key in $S$ and return.

- Else, select a key $p$ called a **pivot** uniformly at random from $S$. Each key of $S$ is equally likely to be selected as pivot.
	- By comparing $p$ to every other key in $S$, split $S$ into two subsets:
	$$S_< = \{s \in S | s < p\} \text{ and } S_> = \{s \in S | s > p\}$$
	- Then, $|S| = n$ takes $n-1$ key comparisons.

> **Example:** RQS on $S = \{2,8,7,1,3,4,6,5\}$.
> Suppose our pivot is $4$. Then:
> $S_< = 2,1,3$, and $S_> = 8,7,6,5$.
> We recursively call on $S_<$ and have pivot $3$. Then $S_< = 2,1$ and $S_> = \emptyset$. Then $p = 1 \implies S_< = \emptyset$ and $S_> = 2$ and print the pivot, going 'up' from where the recursion comes from.
> We do a similar recursive call on $S_>$ for $p = 4$, going 'down'.

**Important Notes:**

- Two keys are compared **only if** one of them is selected as a pivot.

- Two keys are compared **at most once**.

- If two keys are **'split apart'** in different sets by a pivot, then they are **never** compared.


#### Complexity Analysis

- Fix some input $S$ with $n$ distinct keys.

- Run `RQS(S)`.

- Let $C =$ the number of key comparisons done by `RQS(S)`.
The **worst-case value** of $C$ is:
$$C = (n-1) + (n-2) + ... + 2 + 1 = \frac{n(n-1)}{2} \in \Theta(n^2),
$$
when the pivot is the largest item in the set (then you must sort through $n-1$ keys, then $n-2$, etc.)

##### Complexity Analysis of Expected Value
How about the **expected/average value** of $C$ (over all possible random pivot selections)?
The answer is not as obvious as the worst-case value.

To find this, we must use two lemmas:
**Lemma 1.** $E(C) = \sum_{i \leq i < j \leq n} P(z_i, z_j$ are compared$)$.
**Lemma 2.** For $i < j$, $P(z_i, z_j$ are compared$) = \frac{2}{j-i + 1}$.

Then, we can combine the lemmas to get $E(C) \in O(n \log n)$.


###### Lemma 1
We want to show $E(C) = \sum_{i \leq i < j \leq n} P(z_i, z_j$ are compared$)$.

- Let $z_1 <z_2 < ... < z_i < ... z_j < ... < z_n$ be the keys of $S$ in ascending order.

- Run `RQS(S)`, and note that it compares $z_i$ and $z_j$ at most once - and only if $z_i$ or $z_j$ are pivots. Then, let $c_{ij}$ be our **indicator random variable**, where:
$$c_{ij} = \begin{cases}1 & RQS(S) \text{ compares } z_i, z_j \\
0 & \text{otherwise}
\end{cases}$$

- The **total** number of key comparisons done by `RQS(S)` is:
  $$C = \sum_{1 \leq i \leq j \leq n} c_{ij}$$
  - To compute $E(C)$, we can simply just compute $E(c_{ij})$.$$\begin{aligned}
    E(c_{ij}) & = 1 \cdot P(c_{ij} = 1) + 0 \cdot P(c_{ij} = 0)\\
    & = P(c_{ij} = 1)\\
    & = P(z_i, z_j\text{ will be compared})\\
    E(C) & = E\left(\sum_{i \leq i < j \leq n} c_{ij}\right)\\
    & = \sum_{1 \leq i < j \leq n} E(c_{ij}), \text{ by linearity of expectations}\\
    & = P(z_i, z_j\text{ will be compared}
    \end{aligned}$$

###### Lemma 2
We want to show that for $i < j$, $P(z_i, z_j$ are compared$) = \frac{2}{j-i + 1}$.
**Intuition.** 

- For $i=1$ and $j=n$, $P(z_1, z_n$ are compared$) =\frac{2}{n}$, since $z_1$ and $z_n$ are the smallest and largest elements in $S$. They can only be compared if the first pivot among $n$ elements is $z_1$ or $z_n$.
	- Note that $j - i + 1 \to n - 1 + 1 = n$ as required by the lemma.

- Then, for any $i$ and $j = i + 1$, $P(z_i, z_j$ are compared$) = 1$.

**Proof.** Consider the set of keys $Z_{ij} = \{z_i, z_{i+1}, ..., z_j\}$. We have:

- $|Z_{ij}| = j - i + 1$.

- Initially, $Z_{ij}$ is entirely contained in $S$.

- `RQS(S)` selects pivots and uses them to split $S$ into smaller and smaller subsets until it gets subsets of size $1$ or $0$.

- As long as `RQS(S)` selects pivots that are not in $Z_{ij}$, then $Z_{ij}$ remains contained in one of the subsets formed by the pivots, and $z_i, z_j$ will not be compared.

- At some point `RQS(S)` must select a pivot $p$ in $Z_{ij}$. Then, there are two possible cases:
	1. If $z_i < p < z_j$, then $z_i, z_j$ are **never** compared.
	2. If $p = z_i$ or $z_j$, then they are compared.

- Hence:
  $$\begin{aligned}
  P(z_i, z_j \text{ are compared}) & = P(p = z_i \text{ or } p = z_j \mid p \in Z_{ij})\\
  & = \frac{2}{j - i + 1}
  \end{aligned}$$
  We know the inequality will hold since $|Z_{ij}| = j - i + 1$, and each key in $Z_{ij}$ is equally likely to be the selected pivot $p$.



###### Combining Lemmas
$$\begin{aligned}
E(C) & = \sum_{i \leq i < j \leq n} \frac{2}{j - i + 1}\\
& \leq 2n(1 + \frac{1}{2} + \frac13 + ... + \frac1n), \text{ from CLRS p. 184}.
\end{aligned}$$By Harmonic series, $H_n \in O(\log n)$. Hence:
$$E(C) \leq 2n \cdot \log(n) \in O(n \log n)$$


# 4 - Disjoint Sets


### Disjoint Sets
A disjoint set has $n$ distinct elements name $1,2, ..., n$.
Initially, each element is in its own set:
$$S_1 = \{1\}, \ S_2 = \{2\},\ ..., \ S_n = \{n\}$$
Each set $S_x$ has a representative element $x$.


#### Union and Find Operations

- **Union($S_x, S_y)$:** Create a set $S = S_x \cup S_y$ and return the representative of $S$.
Each Union reduces the number of sets by $1$. Then, we can do at most $n-1$ unions.

- **Find($z$):** Return the set that contains the representative $z$.

> **Example:** Suppose we have $S_j$, represented by $j$.

| Operation       | $S_1$     | $S_2$ | $S_3$ | $S_4$ | $S_5$ |
| --------------- | --------- | ----- | ----- | ----- | ----- |
| `Union(S3, S4)` | 1         | 2     | 3, 4  | X     | 5     |
| `Find(4)` = 3   |           |       |       |       |       |
| `Union(S2, S3)`   | 1         | 2,3,4 | X     | X     | 5     |
| `Union(S1, S2)`   | 1,2,3,4   | X     | X     | X     | 5     |
| `Union(S1, S5)`    | 1,2,3,4,5 | X     | X     | X     | X      |

Let $\sigma$ be the sequence of $n-1$ Unions mixed with $m \geq n$ Finds. 
The goal is to  

#### Data Structures for Disjoint Sets

##### 1. Linked Lists
We can store one list per set, and store a **head pointer** and **tail pointer** for each set.
The first element of the set is the representative.

- **Union:** $O(1)$

- **Find:** $O(n)$
Then, the worst case cost of $\sigma: O(n \cdot 1 + m \cdot n) = O(n + mn)$. This is expensive!


##### 2. Augmented Linked Lists
In addition to linked lists, each element also points to its representative.
Then, 

- **Find:** $O(1)$

- **Union:** $O(n)$  - (to link all pointers to the new representative).
Worst-case cost of $\sigma$: $O(n \cdot n + m \cdot 1) = O(n^2 + m)$. This is also expensive.


##### 3. Augmented Linked Lists with Weighted Union
**Weighted Union (WU) Rule:** Append the **smaller** list onto the **bigger** list; keep track of the size of each list.

- **Find:** $O(1)$

- **Union:** $O(n)$
The worst-case cost of executing $\sigma$ is actually smaller! $\sigma: O(m + n \log n)$.

**Proof:** In tutorial!


##### 4. Forest Structure
Each set is represented by a tree, and each node contains one element. Each non-root node will point to its parent, and the root is the set representative.

- **Find:** Follow the path from $x$ up to the root, return the pointer to the root. Cost: $O(1 +$ length of the Find path)

- **Union:** Just need to move the root of one tree to the set it is joined by. Cost: $O(1)$.


###### Decreasing $\sigma$
**Heuristic 1:** Weighted Union (WU) by Size (where size is the number of nodes in the tree).
**WU Rule** by size is that the smaller size tree becomes the child of the bigger size tree.
Then, with WU:

- Any tree $T$ created during the execution of $\sigma$ has height at most $\log_2 n$.

- The worst-case cost of executing $\sigma$ is $O(n + m \log n)$.

>**Lemma.** With WU, any tree $T$ of height $h$ created during the execution of $\sigma$ has at least $2^h$ nodes, i.e., $|T| \geq 2^h$.
>
>**Proof.** Do induction on $h$.
>Let $h=0$. Any tree of height $0$ has at least $2^0 = 1$ node.
>Suppose the lemma holds for $h \geq 0$. Then, we WTS it holds for $h + 1$.
>
>Suppose $A$ is the smaller set, and $B$ is the bigger tree. By IH, $|A| \geq 2^h$, and $|B| \geq |A|$. Therefore, $|B| \geq 2^h$, and then $|T| = |A| + |B| \geq 2^h + 2^h = 2^{h+1}$ nodes.
>
>**Corollary:** With WU, any tree $T$ created during the execution of $\sigma$ has height $h \leq \log_2 n$.
>**Theorem.** With WU, executing any sequence $\sigma$ of $n-1$ Unions mixed with $m \geq n$ Finds takes $O(m \log n)$ time.


TODO WEDNESDAY LECTURE

# 6 - Graph Algorithms


### Graphs
Recall the definition of a graph $G = (V, E)$, with $V$ being the set of vertices, and $E$ being the set of edges, with $n$ being the number of nodes, and $m$ being the number of edges.
**Undirected graphs** - A graph where each edge is an **unordered** pair $(u,v)$ (i.e., $(u, v) = (v,u)$).
**Directed graphs -** Each edge is an **ordered** pair $(u,v)$.


#### Representing Graphs
We can store graphs in **Adjacency Lists** of $G = (V, E)$, where each node is a list that has a linked list of its edges.
We have an Array `Adj[1..n]` of $n$ lists, one for each node $u \in V$, such that `Adj[u]` is the list of all nodes $v$ such that $(u, v) \in E$.

The total size of these lists is $\Theta(n+m)$. Note that $m \leq n^2$.


We can also use **Adjacency matrices**, which are $n \times n$ matrices $A$ such that, for $1 \leq i, j \leq n$: $$\text{A[i, j]}, \begin{cases}1 & \text{If } (i,j) \in E \\ 0 & \text{Otherwise} \end{cases}$$
Adjacency matrices of an undirected graph is **symmetric** about its diagonal. Directed graphs are not necessarily symmetric.
The total size is $\Theta(n^2)$.


##### When to Use Each Representation
For sparse graphs (i.e., $m < n^2$), use an **adjacency list** (it is more space efficient).
To find whether edge $(u, v)$ is in the graph:

- Matrix: $O(1)$

- List: $O(n)$


#### Graph Algorithms

##### Search

1. Start at a node and explore it (i.e., follow its edges to discover new nodes.)

2. With each newly discovered node, explore them (following the edges from those nodes, etc.)
The graph search reveals structural properties of the graph $G$:

- Is $G$ connected?

- Does $G$ have a cycle?

- Shortest path info


###### Breadth First Search
BFS starts at a node $s$.

1. Explore $s$

2. Explore the discovered nodes in the **order of their discovery**.
	The ==First Discovered-First Explored"== (FIFO) policy.
	To do so, put them in a **queue** and explore them in FIFO order.
Complete (2) until all discovered nodes are explored.

BFS algorithms maintain the following information for each node $v$:

- $color[v] = \begin{cases} \text{White,} & \text{Undiscovered} \\ \text{Grey,} & \text{Discovered, not explored} \\ \text{Black,} & \text{Discovered and explored} \end{cases}$

- $p[v] = u$: Node $v$ was discovered while exploring $u$ (i.e., $u$ discovered $v$).

- $d[v]$: The length of the **discovery path** from $s$ (i.e., $s \to u_1 \to u_2 \to ... \to u \to v$)
	- Clearly, $d[v] = d[u] + 1$.

**Algorithm**
```pseudocode
BFS(G, s):
	color[s] = grey;
	d[s] = 0;
	p[s] = NULL;
	
	for (v in V - {S}):
		color[v] = white;
		d[v] = infty;
		p[v] = NULL;
	Q = [];     // Q = nodes that are discovered but not explored.
	ENQ(Q, s);
	
	while (Q is NOT empty) {
		u = DEQ(Q);     // Explore u
		for ((u,v) in E) {     // Explore edge (u,v)
			if (color[v] = white) {      // v is first discovered
				color[v] = grey;
				d[v] = d[u] + 1;
				p[v] = u;
				ENQ(Q, v);
			}
		color[u] = black;
		}
	}
```
The worst-case time complexity of BFS is $O(|V| + |E|)$.


####### Proof of Correctness
Suppose we execute `BFS(s)` on a graph $G$. For every node $v$ of $G$:

- $v$'s **discovery** path from $s$ is $s \to u_1 \to u_2 \to ... \to u \to v$.
	- The length of the discovery path is $d[v]$.

- $v$'s **shortest** path from $s$ is $s \to v_1 \to v_2 \to ... \to v_k \to v$.

> **Lemma 0**. $d[v] \geq \delta(s,v)$.

> **Lemma 1.**
> 	If $u$ enters $Q$ **before** $v$ enters $Q$ during the execution of `BFS(s)`, then $d[u] \leq d[v]$.
> **Proof.** By contradiction, assume Lemma 1 is false.
> 	Let $v$ be the **first** node that enters $Q$ such that $d[u] > d[v]$ for some node $u$ that enters $Q$ before $v$. Then,
> 		$v \neq s$, since no vertex $u$ enters $Q$ before $s$.
> 		$u \neq s$, because $d[s] = 0$ and $d[v] \geq 0$.
> 			This implies that $u$ and $v$ entered $Q$ during the exploration of some nodes, say $u'$ and $v'$ respectively.
> 			Then, $d[u] = d[u'] + 1$ and $d[v] = d[v'] + 1$.
> 		Since $d[u] \neq d[v]$, $d[u'] \neq d[v'] \implies u' \neq v'$ (i.e., $u'$ and $v'$ are distinct nodes).
> 		$u$ was discovered before $v$ $\implies$ $u'$ was explored before $v'$ and $u'$ entered $Q$ before $v'$. 
> 			So, $d[u'] \leq d[v']$ by definition of $v$ $\implies d[u'] + 1 \leq d[v'] + 1 \implies d[u] \leq d[v]$; which is a contradiction.

> **Theorem.**
> 	After `BFS(s)`, for every $v \in V$: $d[v] = \delta(s,v)$.
> 		That is, the **discovery** path to $v$ is a **shortest** path to $v$.
> **Proof.**
> 	By contradiction, suppose there exists $v \in V$ such that $d[x] \neq \delta(s, x)$. Then, $x \neq s$.
> 	Let $v$ be the **closest** node from $s$ such that $d[v] \neq \delta(s, v)$.
> 		By Lemma 0, $d[v] > \delta(s,v)$.
> 	Consider some **shortest** path in $s$ to $v$ in $G$.
> 		Let $(u,v)$ be the last edge on that path. Clearly $\delta(s,v) = \delta(s,u) + 1$.
> 	Since $u$ is closer to $s$ than $v$, $d[u] = \delta(s,u)$, by definition of $v$.
> 		Hence $d[v] > \delta(s,v) = \delta(s,u) + 1$, and $d[v] > d[u] + 1 \ (*)$
> 	
> 	Now consider the **colour** of $v$ just before $u$ is explored. There are $3$ possible cases:
> 		1. $v$ is white:
> 			   When $u$ is explored, $u$ discovers $v$. So, $d[v] = d[u] + 1$, which contradicts $(*)$.
> 		2. $v$ is black:
> 			   $v$ is explored before $u$ is explored, so $v$ entered $Q$ before $u$ enters $Q$.
> 			   By Lemma 1, $d[v] \leq d[u]$, which contradicts $(*)$.
> 		3. $v$ is grey:
> 			   There is some node $w$ that discovered $v$ before $u$ is explored. Then, $w$ is explored before $u$ (a), and $d[v] = d[w] + 1$ (b).
> 				   (a) $\implies$ $w$ enters $Q$ before $u$ $\implies $d[w] \leq d[u]$ (by Lemma 1).
> 				        $\implies$ $d[w] + q \leq d[u] + 1$
> 				   (b) $\implies$ $d[v] \leq d[u] + 1$, which contradicts $(*)$.

**Therefore,** the `BFS(s)` **discovery path** from $s$ to $v$ is a **shortest path** from $s$ to $v$.


###### Depth First Search (DFS)
Recall:

- BFS - First discovered $\to$ First explored

- DFS - Last discovered $\to$ First explored.

The algorithm keeps track of:

- `color[v]` = white, grey, black

- `p[v]` = $u \iff$ $u$ discovered $v$ 

- `d[v]` = 'time' when $v$ is discovered

- `f[v]` = 'time' when $v$'s exploration is completed
To keep track of 'time', it uses a counter which is incremented by $1$ ...

- Whenever a new node is discovered.

- Whenever it finishes exploring a node.

```pseudocode
DFS(G):
	for (v in V):     # initialization
		color[v] = white;
		d[v] = infty;
		f[v] = infty;
		p[v] = NIL;
	time = 0     # note: must be global variable
	
	for (v in V):     # exploration
		if (color[v] = white):
			DFS-Explore(G, v);
```
```pseudocode
DFS-Explore(G, u):
	color[u] = grey;
	time = time + 1;
	d[u] = time;
	for (edge(u,v) in E):
		if (color[v] = white):
			p[v] = u;
			DFS-Explore(G, v);
	color[u] = black;
	time = time + 1;
	f[u] = time;
```
Every edge that does **not** lead to a discovery becomes dotted.

The worst-case time complexity is:
$$\begin{aligned}
O(|V| + |E|) & = O(n + m)
\end{aligned}$$


####### Properties

- **DFS Forests**: DFS' that have the solid edges (i.e., the path of discoveries from a root).
	- If $u_1$ discovers $u_2$, then $u_1$ is an **ancestor** of $u_2$, and $u_2$ is a **descendant** of $u_1$.
	  Then, we have $d[u_1] < d[u_2]$.
Note that these can be **nested** as well.


- **Edge Classification:** 
  An edge $(u,v)$ of $G$ is a:
	- **Tree edge** $\iff$ $u$ is the **parent** of $v$ in the DFS forest.

- **Non-tree edge** $(u,v)$ of $G$ is a:
	- **Forward edge** $\iff$ $u$ is an **ancestor** of $v$ in the DFS forest.
	- **Back edge** $\iff$ $u$ is a **descendant** of $v$ in the DFS forest.
	- **Cross edge** $\iff$ $u$ is **neither** a descendant or an ancestor of $v$ in the DFS forest.

> **Claim 1:** 
> 	$u$ is an ancestor of $v$ in a DFS of $G$ $\iff$ $d[u] < d[v] < f[v] < f[u]$.

> **Claim 2:**
> 	For any $2$ nodes $u, v$, we CANNOT have $d[u] < d[v] < \underline{f[u] < f[v]}$.

> **Claim 3:**
> 	If $(u, v) \in E$, then $d[v]< f[u]$. Then, $v$ is surely discovered **before** we finish exploring $u$.


**Claim:** In a DFS of a directed graph $G = (V, E)$, each edge $(u,v) \in E$ is a:

- **Tree** or **Forward Edge** $\iff d[u] < d[v] <f[v] <f[u]$.

- **Back Edge** $\iff d[v] < d[u] < f[u] < f[v]$.

- **Cross Edge** $\iff d[v] < f[v] < d[u] < f[u]$.
	- $d[u] < f[u] < d[v] <f[v]$ is not possible by Claim 2.



#### Wednesday LEC TODO


#### Minimum Spanning Tree (MST)
Recall:

- **Tree** - A connected undirected graph with no cycles.
	- A tree with $n$ nodes has $n-1$ edges.
	- Adding **any** edge to a tree creates a unique **cycle** containing that edge. Removing any edge from that cycle will result in a tree again.


##### Spanning Trees
Let $G = (V,E)$ be an undirected connected graph.
The **Spanning Tree** of $G$ is the tree $T$ that connects (i.e., spans) all the nodes of $G$, i.e., $$T = (V, E') \text{ with } E' \subseteq E$$
Let $G = (V, E)$ be a **weighted** undirected connected graph.
The **Minimum Spanning Tree** is a spanning tree with the minimum weight on its edges; where the weight of a spanning tree $T$ of $G$ is the total weight of its edges, denoted as $w(T)$.

Network design applications: Computer communication, transportation networks; electrical grids.


###### MST Construction
**Input:** A weighted undirected connected graph $G(V, E)$.
**Output:** A minimum spanning tree $T$ of $G$.


####### **Brute force algorithm:**

- Find every spanning tree of $G$, compute its weight, and return one with the minimum weight.

- But this is very inefficient!
	- For example, if $G$ is a **complete** weighted graph with $n$ nodes, $G$ has about $n^{n - 2}$ different spanning trees.


####### Spanning Forests
A **spanning forest** of $G = (V,E)$ are fragments of a spanning tree of $G$.
That is, it is a set of trees $T_1, T_2, ..., T_k$ such that all of the trees' vertices are a partition of $V$ and all $E' \subseteq E$.


##### MST Construction Theorem
Suppose MST $T$ of $G$ contains the spanning forest $T_1, T_2, ..., T_k$ of $G$.
Let $(u,v)$ be an edge of $G$ of minimum weight between $T_i$ and the other trees of the spanning forest $u \in V_i$ and $v \in V - V_i$.

- Then, there must be an MST $T^*$ of $G$ that contains $T_1, T_2, ..., T_k$ **and** edge $(u,v)$.

> **Proof.** If the MST $T$ also contains $(u,v)$, then we are done: $T^* = T$.
> Suppose MST $T$ does **not** contain $(u,v)$:
> - Let $T' = T + (u,v)$ (i.e., add $(u,v)$ to $T$).
> - By Fact 2, graph $T'$ has a cycle $C$ that contains $(u,v)$.
> 	- Since $u \in V_i$ and $v \in V - V_i$, then $C$ has another edge $(u', v')$ such that $u' \in V_i$ and $v\ \in V - V_i$.
> 	- By choice of $(u,v)$: $w(u,v) \leq w(u', v')$. Then, we can remove one edge of the MST $(u', v')$ since its weight is $\geq (u,v)$.
> - Let $T* = T' - (u', v') = T + (u,v) - (u', v')$. Note that:
> 	(a) $T^*$ is a **spanning tree** (by Fact 2).
> 	(b) $T^*$ contains $T_1, T_2, ..., T_k$ and $(u,v)$.
> 	(c) $w(T^*) = w(T) + w(u,v) - w(u', v')$.
> 		Since $w(u,v) \leq w(u', v')$, we know it will be either negative or $0$. Hence:
> 		$w(T^*) \leq w(T)$. But, $T$ is an **MST** of $G$. So, $T^*$ is also an MST of $G$. 


###### Kruskal's MST Algorithm
Given a connected undirected weighted graph $G = (V,E)$ where:

- $V = \{1,2,..., n\}$

- $E$ : Array of $m$ weighted edges;

```
KruskalMST(G):
	BuildMinHeap(E)     // Turn E into a Min Heap: min-weighted edge at the top.
	for (i = 0 to n):
		MakeSet(i)     // Build forest of n singleton sets {1}, {2}, ...,
	MST_Edges = EmptySet
	while (MST_Edges < n - 1):
		(u, v) = Extract_Min(E)     // Smallest edge not examined yet.
		r = Find(u)
		s = Find(v)
		if r != s:     // If u and v are in different sets
			Union(r, s)
			MST_Edges = MST_edges UNION {(u,v)}
```


####### Runtime Analysis

- `BuildMinHeap()` - $O(m)$

- `MakeSet` - $O(m)$

- While loop:
	- $m$ `ExtractMin`'s $\implies$ $O(m \log n)$ 
	- `Union/Find` (forest implies WU and PC)
		- $n - 1$ `Union`'s $\implies$ $2M$ `Find`'s $\implies$ $O(M \log^* n)$ $\implies O(m \log^* n)$

Hence, the total time complexity of Kruskal's algorithm is $O(m \log n)$.

####### Example
Suppose we have a graph with the following edges after being sorted (note: this take $O(m \log n)$ time):

| Edge | Weight |
| ---- | ------ |
| AB   | 1      |
| CD   | 1      |
| BD   | 2      |
| BC   | 2      |
| ED   | 4      |
| EA   | 5      |
| EC   | 6      |
| EB   | 7       |
	
We can create the following MST:

| Min. edge examined so far | In MST?              | Forest Trees So Far |
| ------------------------- | -------------------- | ------------------- |
|                           |                      | {A} {B} {C} {D} {E} |
| (A,B)                     | Yes                  | {A,B} {C} {D} {E}   |
| (C, D)                    | Yes                  | {A,B} {C,D} {E}     |
| (B, D)                    | Yes                  | {A, B, C, D} {E}    |
| (B, C)                    | No (Creates a cycle) |                     |
| (E,D)                     | Yes                  | {A, B, C, D, E}     |


###### Prim's Algorithm

- Start with any node and extend this node into a bigger and bigger tree.

- At each step, extend the current tree by selecting the 'smallest' edge out of the tree.

# 5 - Amortized Analysis (CLRS 16)


### Amortized Analysis
Given a data structure with operations $T(m)$ and $\frac{T(m)}{m}$, where:

- $T(m)$ is the worst-case **cost** of completing any sequence of $m$ operations; and

- $\frac{T(m)}{m}$ is the average cost of an operation in the worst case,
We want to determine the values of $T(m)$ and $\frac{T(m)}{m}$. In this course, we use:

1. Aggregate Analysis

2. Accounting Method


#### Aggregate Analysis


#### Accounting Method
To evaluate the average cost, each operation is charged the same, even if the actual cost of the operation is different, resulting in the **amortized cost**. For any arbitrary amortized costs, we want the invariant to always hold regardless of the number of operations we do.

> **Example:** Incrementing a $k$-bit binary counter.
> Suppose a binary counter starts at $0$; the running time of the operation is proportional to the number of bits flipped.
> 
> **Intuition:**
> 	Setting a $0$-bit to $1$ costs $2.
> 		- $1 for setting up the bit.
> 		- $1 acting as credit if the bit must be reset to $0$.
> 	Hence, if a bit needs to be rest to $0$, it will cost nothing.
> 
> When incrementing, resetting bits to $0$ always costs $0. By properties of a binary, **at most** one bit will be set to $1$, which we know takes a cost of $2.
> The number of $1$-bits is never negative, and the amount of credit is always non-negative.
> 
> Hence, for $n$ operations, the total amortized cost is $O(n)$, bounding the total actual cost.




### Dynamic Tables
Suppose we have a table $T$ with contiguous blocks of memory, and operations `Insert` and `Delete`.
We have the **Load Factor** $\alpha$:
$$\alpha(T) = \frac{\text{ \# items stored in } T}{\text{size}(T)}$$


##### Table Expansion
Suppose $\alpha(T) = 1$. Then, the table is full. How can we insert another element into the table?

**Table Expansion** allows us to insert new elements by dynamically expanding a table.

1. Allocate new table $T$ larger than $T$.
	- Typically, `size(new T) = 2 size(T)`

1. Copy all items of $T$ into the new $T$.

2. Insert the new element into the new $T$.
With this scheme, $\alpha(T) \geq \frac{1}{2}$ (i.e., no more than half the space is wasted).

The cost of table expansion is `size(T) + 1` ($1$ being the cost of inserting 1 more element). Each new insert until $\alpha(T)$ for the new table costs $1$ until the table needs to be expanded again.


###### Amortized Analysis
Starting with an empty table $T$ of size $1$, what is the total cost of $n$ successive `Insert`'s into $T$?

> **Example:** $n=25$
> Total Cost:
> $$\begin{aligned}\text{Cost of Inserting Elements} & + \text{Cost of table expansion}\\
25 & + 1 & \text{Size is 2.}\\
& + 2 &\text{Size is 4.}\\
& + 4 & ... \\
& + 8 & ...\\
& + 16 & \text{Size is now 32! We can stop.}
 \end{aligned}$$
 > The total cost of $25$ inserts is $25$ + all powers of $2$ smaller than $25$.
 
 
Hence, the total cost of $n$ inserts is equal to $n$ + all powers of $2$ smaller than $n$.
That is:
$$\begin{aligned}\text{Total cost of }n \text{ inserts} & \leq n + \sum_{k=0}^{k=\lfloor \log_2 n \rfloor} 2^k & = n + \left(2^{\lfloor \log_2n \rfloor + 1} - 1\right) & \leq n + 2 \cdot 2^{\lfloor\log_2 n \rfloor}\\
& \leq n + 2n\\
& \leq 3n\\
\\
\text{Amortized cost per Insert} & \leq \frac{3n}{3} = 3\end{aligned}$$


###### Accounting Method
Recall if:

- $c_i$: **Actual** cost of $i$'th operation.

- $\hat{c_i}$: Cost **charged** for the $i$'th operation.
We require $\sum_{i=1}^n \hat{c_i} \geq \sum_{i=1}^n c_i$ for all sequence of $n$ operations.

`Insert(x)`:

- $1 charge for inserting $x$.

- $1 credit on $x$ (for copying $x$ over).

- $1 credit on $a$ (for copying $a$ over).
Hence, there is a total of $3 being charged with every insert.
When the table is full, the **Total Credit** is the number of elements in the Table.
On the next insert, we must use our credits to move elements into the new table.

Let $\sigma$ be the sequence of $n$ inserts, starting from an empty table $T$ of size $1$.
TODO

`Delete`:
**Problem:** After deleting items, $\alpha(T)$ decreases $\implies$ Memory waste increases.
If $\alpha(T)$ becomes too small, reduce memory waste by:

1. Allocating a new smaller table.

2. Copying all the items to the new table.

> When is $\alpha(T)$ too small? How small should the new table be?

We want:

1. $\alpha(T) \geq$ constant $c$ (to reduce memory waste).

2. Amortized cost per operation (insert/delete) is $O(1)$.

So we argue that if $\alpha(T) = \frac{1}{4}$ and `Delete` occurs, size(new $T$) $= \frac{1}{2}$ size($T$)
Then, it is ensured that $\alpha(T) \geq \frac{1}{4}$.

- $\sigma$: Arbitrary sequence of $n$ Inserts and Deletes, starting from empty table $T$ of size $1$.
What is the amortized cost?

A sequence of `Insert`'s,  `Delete`'s applied to $T$ may cause:

- **Expansion:** $3 for each Insert (i.e., $\frac{n}{2} \cdot \$ 2 = \$n$ credit).

- **Contraction:** $2 for each Delete
	- $\geq \frac{n}{4}$ deletes with the cost of copying items into new $T = \frac{n}{4}$.
	- Then, it costs $1 + $1 credit for future contractions.
		- Hence: $\frac{n}{4} \cdot \$1 = \$\frac{n}{4}$ credit


