# CS61A (Python)

- How to run doctest in Python
 - if python3 -m doctest ...py is not working
 - try python3 -m doctest -v ...py

## Lecture 10

### Sequence Aggregation

- any(iterable) -> bool
- all(iterable) -> bool

a = [1,2,3]<br>
a1 = [0,1,2,3]


all(a) -> True   

all(a1) -> False   

any(a1) - >True   

### Tree Abstraction

![Tree Abstraction](/images/Tree.png)

```python
# Constructor
def tree(label, branches=[]):
	"""
	label is the value in it
	branches are its children
	"""
	for branch in branches:
		assert is_tree(branch)
	return [label] + list[branches]

# Selectors
def label(tree):
	return tree[0]

def branches(tree):
	# a = [1,2,3], a[1:] = [2,3]
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches:
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	# if tree is a leaf -> branch(tree) = return [] = False => return True
	return not branches(tree)

```

### Tree Processing

![Tree Processing](images/TreeProcess.png)

```python
def count_nodes(t):
	if is_leaf(t):
		return 1
	total
	for b in branches:
		total += count_nodes(n)
	return total + 1

def collect_leaves(t:
	if is_leaf(t):
		return [lable(t)]
	res = []
	for b in branches:
		res += collect_leaves(b)
	return res

```