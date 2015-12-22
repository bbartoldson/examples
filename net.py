from math import sqrt, pi, sin
import random
import numpy
import matplotlib.pyplot as plt

a = 2
b = 3
c = -4
d = 0

da=0
db=0
dc=0
dd = 0

a1 = 1
a2 = 2
b1 = 3
b2 = 4
c1 = 1
c2 = 3

da1 = 0
da2 = 0
db1 = 0
db2 = 0
dc1 = 0
dc2 = 0

avg_error = 0

for x in range (1, 50000):

	input = random.uniform(-pi, pi)
	act = sin(input)

	#update and predict
	a += da
	b += db
	c += dc
	d += dd

	a1 += da1
	a2 += da2
	
	b1 += db1
	b2 += db2

	c1 += dc1
	c2 += dc2

	a_stuff = a1*input + a2
	b_stuff = b1*input + b2
	c_stuff = c1*input + c2

	predict = a * max(0, a_stuff)  + b * max(0, b_stuff) + c * max(0, c_stuff) + d
	
	error = (act - predict) ** 2
	avg_error += error

	if (x % 5000 == 0):
		avg_error /= 3000
		print(avg_error)
		avg_error = 0
	
	step = .0001
	sign = numpy.sign(act - predict)

	if (a_stuff > 0):
		da = step * a_stuff * sqrt(error) * sign	
		da1 = step * a * input * sqrt(error) * sign
		da2 = step * a * sqrt(error) * sign
	if (b_stuff > 0):
		db = step * b_stuff * sqrt(error) * sign
		db1 = step * b * input * sqrt(error) * sign
		db2 = step * b * sqrt(error) * sign
	if (c_stuff > 0):
		dc = step * c_stuff * sqrt(error) * sign
		dc1 = step * c * input * sqrt(error) * sign
		dc2 = step * c * sqrt(error) * sign
	dd = step * sqrt(error) * sign

test = []
out = []

for y in range (100):
	
	input = -pi + y * 2 * pi / 99

	test.append(input)

	output = a * max(0, a1*input + a2) + b * max(0, b1*input + b2) + c * max(0, c1* input + c2)
	
	out.append(output)


plt.plot(test, out)
plt.show()	
