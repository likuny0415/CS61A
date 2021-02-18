
def keep_ints(cond, n):
	i = 1
	while i <= n:
		if cond(i):
			print(i)
		i += 1
	return

def make_keeper(n):
	def func(x):
		i = 1;
		while i <= n:
			if x(i):
				print(i)
			i += 1
		return;
	return func;

