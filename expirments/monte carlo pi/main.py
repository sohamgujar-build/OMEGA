import random
random.seed(6)

inside =0
total = 100000
for _ in range(total):
	x = random.random()
	y = random.random()
	if x * x + y * y <= 1:
		inside += 1
print(inside)
estimate = 4 * inside / total
print(estimate)
