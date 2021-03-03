# Constructor
def tree(label, branches=[]):
	"""
	label is the value in it
	branches are its children
	"""
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

# Selectors
def label(tree):
	return tree[0]

def branches(tree):
	# a = [1,2,3], a[1:] = [2,3]
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	# if tree is a leaf -> branch(tree) = return [] = False => return True
	return not branches(tree)


def count_nodes(t):
	if is_leaf(t):
		return 1
	total = 0
	for b in branches(t):
		total += count_nodes(b)
	return total + 1

def collect_leaves(t):
	#combine list => [put value inside list]
	if is_leaf(t):
		return [label(t)]
	res = []
	for b in branches(t):
		res += [collect_leaves(b)]
	return sum(res, [])

def	print_tree(t, indent=0):

	if is_leaf(t):
		print(' ' * indent, label(t))
	else:
		print(' ' * indent, label(t))
		for b in branches(t):
			print_tree(b, indent + 1)

def square_tree(t):
	if is_leaf(t):
		return tree(label(t) ** 2)

	lst = []
	for b in branches(t):
		lst += [square_tree(b)]
	return tree(label(t) ** 2,lst)

def fib_tree(n):
	if n <= 1:
		return tree(n)
	
	left = fib_tree(n - 2)
	right = fib_tree(n - 1)
	return tree(label(left) + label(right), [left, right])

a = fib_tree(4)		

tree1 = tree(4, [tree(3),
				 tree(2, [tree(1),
				 		  tree(0)])])