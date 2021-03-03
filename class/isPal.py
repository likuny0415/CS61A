# Determine if a list is palindromes
def isPal(x):
	"""
	>>> isPal([1,2,1])
	True
	>>> isPal([1,2])
	False
	"""
	if len(x) <= 1:
		return True
	else:
		if x[0] != x[len(x) - 1]:
			return False
		else:
			return isPal(x[1:(len(x) - 1)])

def isPalN(n, list):
	isPal(list[:n])
