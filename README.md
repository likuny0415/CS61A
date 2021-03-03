# CS61A (Python)

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

![Tree](/images/Tree.png)

```
# Constructor
def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list[branches]

# Selectors
def label(tree):
	return tree[0]

def branches(tree):
	# a = [1,2,3], a[1:] = [2,3]
	return tree[1:]

```