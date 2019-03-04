def calc_root(n, limit):
	'''Calculate using Babylon. Limit is the number of iterations'''
	x1 = 1 
	for i in range(limit):
		x_n_plus_1 = 1/2 * (x1 + (n / x1))
		x1 = x_n_plus_1
	return x1

n = int(input("Введите основание корня: "))

for i in [10, 100, 1000]: # Test on whether accuracy improves with more iterations
	print(calc_root(n, i), '\n')





